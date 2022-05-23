from dataclasses import dataclass
from typing import Optional
import pandas as pd
import os


@dataclass
class MedicalData:
    df: pd.DataFrame
    bnf_code_vmp_nm: dict

    @staticmethod
    def load_csv_files():
        df = pd.DataFrame()
        for file in os.listdir("static"):
            if file.endswith(".csv"):
                temp = pd.read_csv(
                    os.path.join("static", file), encoding="latin1", low_memory=False
                )
                df = df.append(temp)

        bnf_code_vmp_nm = dict(zip(df["BNF Code"], df["VMP_NM"]))

        return MedicalData(df, bnf_code_vmp_nm)

    def avg_gross_cost(self, month: int) -> Optional[float]:
        """Average cost of prescriptions (Gross Cost) in the selected period (month resolution)"""

        return self.df[self.df["Month"] == month]["Gross Cost (£)"].mean()

    def avg_total_items(self, month: int) -> Optional[float]:
        """Average number of products (Total Items) in the selected period (month resolution)"""

        return self.df[self.df["Month"] == month]["Gross Cost (£)"].mean()

    def nunique_bnf_codes(self, month: int) -> Optional[int]:
        """Number of prescriptions in the selected period (month resolution) according to the code (BNF Code)"""

        return self.df[self.df["Month"] == month]["BNF Code"].nunique()

    def product_description(self, bnf_code: str) -> str:
        """Product description (VMP_NM) based on the code (BNF Code)"""

        return self.bnf_code_vmp_nm.get(bnf_code, "Not valid BNF Code")
