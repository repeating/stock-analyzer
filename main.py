from backend.analyzer import Analyzer
import pandas as pd


def main():
    results = Analyzer().analyze()
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(results)


if __name__ == '__main__':
    main()