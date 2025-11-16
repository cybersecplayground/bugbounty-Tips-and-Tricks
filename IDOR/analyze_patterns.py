#!/usr/bin/env python3
import json
import re
import sys
from collections import Counter

def analyze_idor_results(results_file):
    with open(results_file, 'r') as f:
        data = json.load(f)
    
    findings = {
        'high_impact': [],
        'medium_impact': [],
        'low_impact': [],
        'patterns': {},
        'recommendations': []
    }
    
    for result in data.get('results', []):
        url = result.get('input', {}).get('FUZZ', '')
        status = result.get('status', 0)
        length = result.get('length', 0)
        words = result.get('words', 0)
        lines = result.get('lines', 0)
        content = result.get('content', '')
        
        # Analyze response patterns
        impact = assess_impact(status, length, content, url)
        
        if impact == 'high':
            findings['high_impact'].append({
                'url': url,
                'status': status,
                'length': length,
                'sensitive_data': extract_sensitive_data(content)
            })
        elif impact == 'medium':
            findings['medium_impact'].append({
                'url': url,
                'status': status,
                'length': length
            })
        else:
            findings['low_impact'].append({
                'url': url,
                'status': status
            })
    
    # Identify ID patterns
    findings['patterns'] = identify_patterns(findings)
    findings['recommendations'] = generate_recommendations(findings)
    
    return findings

def assess_impact(status, length, content, url):
    """Determine impact level based on response characteristics"""
    
    # High impact indicators
    if status == 200:
        if contains_sensitive_data(content):
            return 'high'
        if length > 1000:  # Substantial data returned
            return 'high'
        if 'email' in content.lower() or 'password' in content.lower():
            return 'high'
    
    # Medium impact indicators
    if status in [200, 201, 202]:
        return 'medium'
    
    # Information disclosure through errors
    if status == 500 and 'sql' in content.lower():
        return 'medium'
    
    return 'low'

def contains_sensitive_data(content):
    """Check if response contains sensitive information"""
    sensitive_patterns = [
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
        r'\b(?:\d[ -]*?){13,16}\b',  # Credit card
        r'password|token|secret|key|auth',  # Credentials
    ]
    
    for pattern in sensitive_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def extract_sensitive_data(content):
    """Extract actual sensitive data from response"""
    sensitive_data = {}
    
    # Extract emails
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
    if emails:
        sensitive_data['emails'] = emails
    
    # Extract potential tokens/keys
    tokens = re.findall(r'[A-Za-z0-9]{32,}', content)  # 32+ char strings
    if tokens:
        sensitive_data['potential_tokens'] = tokens[:5]  # Limit output
    
    return sensitive_data

def identify_patterns(findings):
    """Identify UUID/ID patterns for further testing"""
    patterns = {
        'uuid_patterns': [],
        'numeric_ranges': [],
        'common_prefixes': [],
        'response_trends': []
    }
    
    all_urls = [item['url'] for item in findings['high_impact'] + findings['medium_impact']]
    
    # UUID pattern analysis
    uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    for url in all_urls:
        uuids = re.findall(uuid_pattern, url, re.IGNORECASE)
        patterns['uuid_patterns'].extend(uuids)
    
    # Numeric range detection
    numbers = re.findall(r'\d+', ' '.join(all_urls))
    if numbers:
        num_list = [int(n) for n in numbers if len(n) > 2]  # Ignore small numbers
        if num_list:
            patterns['numeric_ranges'] = {
                'min': min(num_list),
                'max': max(num_list),
                'count': len(num_list)
            }
    
    return patterns

def generate_recommendations(findings):
    """Generate testing recommendations based on patterns"""
    recommendations = []
    
    if findings['patterns']['uuid_patterns']:
        recommendations.append("Test UUID increment/decrement patterns")
        recommendations.append("Try special UUIDs: 00000000-0000-0000-0000-000000000000")
    
    if findings['patterns']['numeric_ranges']:
        range_info = findings['patterns']['numeric_ranges']
        recommendations.append(f"Test numeric range: {range_info['min']} to {range_info['max']}")
    
    if findings['high_impact']:
        recommendations.append("Prioritize these endpoints for detailed testing")
        recommendations.append("Check for mass assignment vulnerabilities")
    
    return recommendations

def print_report(findings):
    """Print a formatted analysis report"""
    print("=" * 60)
    print("IDOR PATTERN ANALYSIS REPORT")
    print("=" * 60)
    
    print(f"\n📊 FINDINGS SUMMARY:")
    print(f"   High Impact: {len(findings['high_impact'])} endpoints")
    print(f"   Medium Impact: {len(findings['medium_impact'])} endpoints") 
    print(f"   Low Impact: {len(findings['low_impact'])} endpoints")
    
    if findings['high_impact']:
        print(f"\n🚨 HIGH IMPACT ENDPOINTS:")
        for item in findings['high_impact'][:3]:  # Show top 3
            print(f"   URL: {item['url']}")
            print(f"   Status: {item['status']}, Length: {item['length']}")
            if item['sensitive_data']:
                print(f"   Sensitive Data: {item['sensitive_data']}")
            print()
    
    if findings['patterns']:
        print(f"\n🎯 DETECTED PATTERNS:")
        if findings['patterns']['uuid_patterns']:
            print(f"   UUIDs Found: {len(set(findings['patterns']['uuid_patterns']))}")
        if findings['patterns']['numeric_ranges']:
            r = findings['patterns']['numeric_ranges']
            print(f"   Numeric Range: {r['min']} - {r['max']} ({r['count']} IDs)")
    
    if findings['recommendations']:
        print(f"\n💡 RECOMMENDED ACTIONS:")
        for rec in findings['recommendations']:
            print(f"   • {rec}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_patterns.py <results.json>")
        sys.exit(1)
    
    results_file = sys.argv[1]
    findings = analyze_idor_results(results_file)
    print_report(findings)
    
    # Save detailed report
    with open('idor_analysis_report.json', 'w') as f:
        json.dump(findings, f, indent=2)
    
    print(f"\n📁 Detailed report saved to: idor_analysis_report.json")
