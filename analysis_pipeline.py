import pandas as pd
from statsmodels.stats.anova import AnovaRM
from scipy.stats import ttest_rel
from statsmodels.stats.multitest import multipletests

def calculate_subject_means(df,value_col):
    subject_means = (
        df.groupby(["subject", "condition"])[value_col]
          .mean()
          .reset_index()
    )

    return subject_means

def summarize_conditions(subject_means,value_col):
    condition_summary = (
        subject_means
        .groupby("condition")[value_col]
        .agg(["mean", "std", "count"])
    )

    return condition_summary

def prepare_rm_complete(subject_means,value_col):
    rm_wide = subject_means.pivot(
        index="subject",
        columns="condition",
        values=value_col
    )

    rm_complete = rm_wide.dropna()

    return rm_complete

def prepare_rm_long(rm_complete,value_col):
    rm_long = rm_complete.reset_index().melt(
        id_vars="subject",
        value_vars=["83cm", "93cm", "103cm"],
        var_name="condition",
        value_name=value_col
    )

    return rm_long

def run_rm_anova(rm_long,value_col):
    anova = AnovaRM(
        rm_long,
        depvar=value_col,
        subject="subject",
        within=["condition"]
    )

    anova_results = anova.fit()

    return anova_results

def run_posthoc(rm_complete):

    comparisons = [
        ("83cm", "93cm"),
        ("83cm", "103cm"),
        ("93cm", "103cm"),
    ]

    results = []

    for cond1, cond2 in comparisons:
        test = ttest_rel(
            rm_complete[cond1],
            rm_complete[cond2]
        )

        results.append({
            "comparison": f"{cond1} vs {cond2}",
            "t": test.statistic,
            "p_raw": test.pvalue
        })

    posthoc_results = pd.DataFrame(results)

    reject, p_corrected, _, _ = multipletests(
        posthoc_results["p_raw"],
        alpha=0.05,
        method="bonferroni"
    )

    posthoc_results["p_bonferroni"] = p_corrected
    posthoc_results["significant"] = reject

    return posthoc_results