"""
FinOps Module: Cross-Cloud Cost Analysis & OCI Optimization
Author: Kelsen Lima | Oracle ACE Apprentice
Date: October 2026
Description: Tracks OPEX/CAPEX optimization across OCI, Azure, GCP, and Huawei workloads.
"""

def calculate_finops_savings(current_spend, oci_optimized_spend):
    savings = current_spend - oci_optimized_spend
    savings_percentage = (savings / current_spend) * 100
    
    return {
        "original_spend_usd": current_spend,
        "oci_optimized_spend_usd": oci_optimized_spend,
        "total_savings_usd": savings,
        "reduction_percentage": f"{savings_percentage:.1f}%"
    }

if __name__ == "__main__":
    print("[FinOps Engine] Evaluating workload rationalization across Multi-Cloud footprint...")
    finops_report = calculate_finops_savings(current_spend=100000, oci_optimized_spend=70000)
    print(f"[FinOps Result]: Achieved {finops_report['reduction_percentage']} cost reduction via OCI FinOps strategy.")