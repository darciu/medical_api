import snowflake.connector


class SnowflakeDataConnector:
    def __init__(self, user: str, password: str, account: str):
        self.user = user
        self.password = password
        self.account = account

    def get_data_one_result(self, query: str) -> str or int:
        ctx = snowflake.connector.connect(
            user=self.user, password=self.password, account=self.account
        )
        cs = ctx.cursor()
        try:
            cs.execute(query)
            one_row = cs.fetchone()
            return one_row[0]
        except:
            return "Connector could not retrieve any data. Chceck your query"
        finally:
            cs.close()
            ctx.close()
