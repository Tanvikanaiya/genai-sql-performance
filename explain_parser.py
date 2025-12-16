import pandas as pd

def parse_explain(explain_output):
    df = pd.DataFrame(explain_output)

    metrics = {
        "tables_scanned": len(df),
        "using_filesort": "Using filesort" in df.to_string(),
        "using_temporary": "Using temporary" in df.to_string(),
        "join_type": df["type"].tolist(),
        "rows_examined": df["rows"].sum()
    }
    return metrics, df
