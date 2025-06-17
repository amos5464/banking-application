from account import Account
from savings_account import SavingsAccount
from current_account import CurrentAccount
import streamlit as st


class BankPages:
    def __init__(self):
        self.setup_page_config()

        if 'savings' not in st.session_state:
            st.session_state.savings = SavingsAccount(20000)
        if 'current' not in st.session_state:
            st.session_state.current = CurrentAccount(1000)

    def setup_page_config(self):
        st.set_page_config(
            page_title="Wayne Bank",
            layout="centered",
            page_icon="🏦"
        )

    def display_header(self):
        st.title("Wayne Bank")
        st.write("---")

    def account_selection(self):
        return st.radio(
            "Select Account",
            ("Savings Account", "Current Account")
        )

    def get_selected_account(self, account_type):
        return st.session_state.savings if account_type == "Savings Account" else st.session_state.current

    def display_balance(self, account):
        balance_display = st.empty()
        with balance_display.container():
            st.subheader("Account Balance")
            st.write(f"Current Balance: {account.balance}")
            st.write("---")
        return balance_display

    def transaction_section(self):
        st.subheader("Perform Transaction")
        operation = st.selectbox("Transaction Type", ("Deposit", "Withdraw"))
        amount = st.number_input("Amount", min_value=100.00, step=100.00, format="%.2f")
        return operation, amount

    def process_transaction(self, account, operation, amount, balance_display):
        try:
            if operation == "Deposit":
                account.deposit(amount)
                st.success(f"""
                Deposit Successful!
                Amount: {amount}
                New Balance: {account.balance}
                """)
            else:
                if account.withdraw(amount):
                    st.success(f"""
                    Withdrawal Successful!
                    Amount: {amount}
                    New Balance: {account.balance}
                    """)
                else:
                    st.error("Withdrawal failed")
            self.update_balance_display(account, balance_display)

        except ValueError as e:
            st.error(f"Transaction Failed: {str(e)}")
            self.update_balance_display(account, balance_display)

    def update_balance_display(self, account, balance_display):
        with balance_display.container():
            st.subheader("Account Balance")
            st.write(f"Current Balance: {account.balance}")
            st.write("---")

    def main_page(self):
        self.display_header()

        account_type = self.account_selection()
        account = self.get_selected_account(account_type)

        balance_display = self.display_balance(account)
        operation, amount = self.transaction_section()

        if st.button("Process Transaction"):
            self.process_transaction(account, operation, amount, balance_display)
            "Amos Oyeyemi did the UI (User interface) and the pages.py "


def main():
    bank_app = BankPages()
    bank_app.main_page()


if __name__ == "__main__":
    main()