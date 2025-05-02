def display_menu():
    print("\n📋 ShopEasy Customer Support Bot")
    print("1. Track Order")
    print("2. Cancel Order")
    print("3. Return/Exchange Item")
    print("4. FAQs")
    print("5. Submit Feedback")
    print("6. Say Hello")
    print("7. Exit")

def chatbot():
    print("👋 Welcome to ShopEasy's Customer Support Bot!")
    feedback_log = []  # Store feedback for simplicity

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            order_id = input("📦 Enter your Order ID: ").strip()
            if order_id:
                print(f"🚚 Order {order_id} is being processed and will arrive soon!")
            else:
                print("⚠️ Please enter a valid Order ID.")

        elif choice == '2':
            order_id = input("🛑 Enter Order ID to cancel: ").strip()
            if order_id:
                print(f"✅ Order {order_id} has been cancelled.")
            else:
                print("⚠️ Please enter a valid Order ID.")

        elif choice == '3':
            order_id = input("🔄 Enter Order ID for return/exchange: ").strip()
            if order_id:
                reason = input("📝 Reason for return/exchange: ").strip()
                if reason:
                    print(f"📨 Return request for Order {order_id} submitted with reason: {reason}.")
                else:
                    print("⚠️ Please provide a reason.")
            else:
                print("⚠️ Please enter a valid Order ID.")

        elif choice == '4':
            print("\n📚 FAQs:")
            print("- Q: How do I track my order?\n  A: Select option 1 and enter your Order ID.")
            print("- Q: Can I cancel a delivered order?\n  A: No, only non-delivered orders can be cancelled.")
            print("- Q: How do I return an item?\n  A: Use option 3 and provide Order ID and reason.")

        elif choice == '5':
            feedback = input("💬 Enter your feedback: ").strip()
            if feedback:
                feedback_log.append(feedback)
                print("🌟 Thank you for your feedback!")
            else:
                print("⚠️ Feedback cannot be empty.")

        elif choice == '6':
            print("😊 Hello! How can I make your shopping experience better today?")

        elif choice == '7':
            print("🙌 Thank you for using ShopEasy's Customer Support Bot. Goodbye!")
            if feedback_log:
                print("\n📜 Feedback Received:")
                for i, fb in enumerate(feedback_log, 1):
                    print(f"{i}. {fb}")
            break

        else:
            print("⚠️ Invalid input. Please choose a number from 1 to 7.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()



# Absolutely! Let’s break down this **ShopEasy Customer Support Bot** step-by-step with clear explanation, concepts, and new terms.

# ---

# ## 🎯 **Objective of the Code**

# To simulate a simple **text-based chatbot** for customer support tasks like tracking orders, cancelling, returning items, answering FAQs, and collecting feedback.

# ---

# ## ✅ **Step-by-Step Explanation**

# ---

# ### **1. `display_menu()`**

# ```python
# def display_menu():
#     print("\n📋 ShopEasy Customer Support Bot")
#     print("1. Track Order")
#     print("2. Cancel Order")
#     print("3. Return/Exchange Item")
#     print("4. FAQs")
#     print("5. Submit Feedback")
#     print("6. Say Hello")
#     print("7. Exit")
# ```

# * 🔹 This function prints a **menu of options** the user can choose from.
# * Called repeatedly inside the chatbot loop to show options.

# ---

# ### **2. `chatbot()`**

# ```python
# def chatbot():
#     print("👋 Welcome to ShopEasy's Customer Support Bot!")
#     feedback_log = []  # Store feedback for simplicity
# ```

# * Displays welcome message.
# * Initializes an empty list `feedback_log` to store customer feedback.

# ---

# ### **3. `while True:` — Infinite Loop**

# This loop ensures that the bot **keeps running** until the user chooses to exit (`option 7`).

# ---

# ### **4. Get User Input**

# ```python
# display_menu()
# choice = input("Enter your choice (1-7): ").strip()
# ```

# * Shows the menu again.
# * Takes input from user and removes leading/trailing spaces with `.strip()`.

# ---

# ### **5. Option-wise Action Handling**

# Let’s now go through each choice:

# ---

# ### 🔸 **Choice 1 — Track Order**

# ```python
# if choice == '1':
#     order_id = input("📦 Enter your Order ID: ").strip()
#     if order_id:
#         print(f"🚚 Order {order_id} is being processed and will arrive soon!")
#     else:
#         print("⚠️ Please enter a valid Order ID.")
# ```

# * Takes Order ID input.
# * If it’s valid (non-empty), confirms it’s being processed.

# ---

# ### 🔸 **Choice 2 — Cancel Order**

# ```python
# elif choice == '2':
#     order_id = input("🛑 Enter Order ID to cancel: ").strip()
#     if order_id:
#         print(f"✅ Order {order_id} has been cancelled.")
#     else:
#         print("⚠️ Please enter a valid Order ID.")
# ```

# * Similar to above, but for cancellation.

# ---

# ### 🔸 **Choice 3 — Return/Exchange**

# ```python
# elif choice == '3':
#     order_id = input("🔄 Enter Order ID for return/exchange: ").strip()
#     if order_id:
#         reason = input("📝 Reason for return/exchange: ").strip()
#         if reason:
#             print(f"📨 Return request for Order {order_id} submitted with reason: {reason}.")
#         else:
#             print("⚠️ Please provide a reason.")
#     else:
#         print("⚠️ Please enter a valid Order ID.")
# ```

# * First checks Order ID.
# * Then asks for a **reason**.
# * If both are given, logs a confirmation.

# ---

# ### 🔸 **Choice 4 — FAQs**

# ```python
# elif choice == '4':
#     print("\n📚 FAQs:")
#     print("- Q: How do I track my order?\n  A: Select option 1 and enter your Order ID.")
#     print("- Q: Can I cancel a delivered order?\n  A: No, only non-delivered orders can be cancelled.")
#     print("- Q: How do I return an item?\n  A: Use option 3 and provide Order ID and reason.")
# ```

# * Just displays predefined Frequently Asked Questions.
# * No user input required.

# ---

# ### 🔸 **Choice 5 — Submit Feedback**

# ```python
# elif choice == '5':
#     feedback = input("💬 Enter your feedback: ").strip()
#     if feedback:
#         feedback_log.append(feedback)
#         print("🌟 Thank you for your feedback!")
#     else:
#         print("⚠️ Feedback cannot be empty.")
# ```

# * Asks user for feedback.
# * If provided, adds to `feedback_log` list.
# * Thanks the user.

# ---

# ### 🔸 **Choice 6 — Say Hello**

# ```python
# elif choice == '6':
#     print("😊 Hello! How can I make your shopping experience better today?")
# ```

# * A friendly greeting.

# ---

# ### 🔸 **Choice 7 — Exit**

# ```python
# elif choice == '7':
#     print("🙌 Thank you for using ShopEasy's Customer Support Bot. Goodbye!")
#     if feedback_log:
#         print("\n📜 Feedback Received:")
#         for i, fb in enumerate(feedback_log, 1):
#             print(f"{i}. {fb}")
#     break
# ```

# * Says goodbye.
# * If there is feedback collected, it prints it before exiting.
# * Ends loop using `break`.

# ---

# ### 🔸 **Invalid Input**

# ```python
# else:
#     print("⚠️ Invalid input. Please choose a number from 1 to 7.")
# ```

# * If user enters something outside `1-7`, shows a warning.

# ---

# ## 📘 Concepts Used

# | Concept             | Explanation                                                         |
# | ------------------- | ------------------------------------------------------------------- |
# | **Function**        | Reusable block of code. e.g., `display_menu()`.                     |
# | **Infinite Loop**   | Loop that runs forever until `break` is called.                     |
# | **List**            | Python data structure to store multiple values (used for feedback). |
# | **Input/Output**    | User input with `input()`, output via `print()`.                    |
# | **String Strip**    | `.strip()` removes extra spaces before/after user input.            |
# | **Conditionals**    | `if`, `elif`, `else` used to decide what action to take.            |
# | **Enumerate**       | Used in feedback display to number items (1, 2, 3, etc.).           |
# | **Break Statement** | Exits the loop when the user chooses to exit.                       |

# ---

# ## 📌 Short Algorithm Summary

# 1. Start the chatbot.
# 2. Show menu repeatedly.
# 3. Take user input.
# 4. Based on input:

#    * Track order / Cancel / Return / FAQs / Feedback / Greet / Exit
# 5. Loop until user exits using option 7.
# 6. On exit, display feedback log if any.

# ---

# Would you like this chatbot to support **multiple feedback entries** or **return/exchange history** in the future?
