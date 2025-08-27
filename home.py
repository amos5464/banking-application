import streamlit as st
from savings_account import SavingsAccount
from current_account import CurrentAccount


def main():
    st.set_page_config(
        page_title="Wayne Bank",
        layout="centered",
        page_icon="🏦"
    )

    if 'savings' not in st.session_state:
        st.session_state.savings = SavingsAccount(20000)
    if 'current' not in st.session_state:
        st.session_state.current = CurrentAccount(1000)

    st.title("Wayne Bank")
    st.write("---")

    account_type = st.radio(
        "Select Account",
        ("Savings Account", "Current Account")
    )

    account = st.session_state.savings if account_type == "Savings Account" else st.session_state.current

    balance_display = st.empty()
    with balance_display.container():
        st.subheader("Account Balance")
        st.write(f"Current Balance: {account.balance}")
        st.write("---")

    st.subheader("Perform Transaction")
    operation = st.selectbox("Transaction Type", ("Deposit", "Withdraw"))
    amount = st.number_input("Amount", min_value=100.00, step=100.00, format="%.2f")

    if st.button("Process Transaction"):
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

            with balance_display.container():
                st.subheader("Account Balance")
                st.write(f"Current Balance: {account.balance}")
                st.write("---")

        except ValueError as e:
            st.error(f"Transaction Failed: {str(e)}")
            with balance_display.container():
                st.subheader("Account Balance")
                st.write(f"Current Balance: {account.balance}")
                st.write("---")


if __name__ == "__main__":

    main()
