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