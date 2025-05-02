import re
from datetime import datetime

class CustomerChatbot:
    def __init__(self):
        self.order_db = {}  # Simulated order database: {order_id: status}
        self.feedback_log = []  # Store feedback with timestamps

    def display_menu(self):
        print("\n🌟 Welcome to ShopSmart Assistant 🌟")
        print("1. Track Order")
        print("2. Cancel Order")
        print("3. Request Return/Exchange")
        print("4. View FAQs")
        print("5. Submit Feedback")
        print("6. Chat with a Greeting")
        print("7. View Feedback History")
        print("8. Exit")

    def validate_order_id(self, order_id):
        # Validate order ID format (e.g., ORD-123)
        return bool(re.match(r'^ORD-\d{3}$', order_id))

    def track_order(self):
        order_id = input("📦 Enter your Order ID (e.g., ORD-123): ").strip().upper()
        if not self.validate_order_id(order_id):
            print("⚠️ Invalid Order ID format. Use format ORD-123.")
            return
        if order_id in self.order_db:
            status = self.order_db[order_id]
            print(f"🚚 Order {order_id} is {status}.")
        else:
            print(f"🔍 Order {order_id} not found. Please check the ID.")
            self.order_db[order_id] = "Processing"  # Simulate adding new order

    def cancel_order(self):
        order_id = input("🛑 Enter Order ID to cancel (e.g., ORD-123): ").strip().upper()
        if not self.validate_order_id(order_id):
            print("⚠️ Invalid Order ID format. Use format ORD-123.")
            return
        if order_id in self.order_db:
            if self.order_db[order_id] != "Delivered":
                self.order_db[order_id] = "Cancelled"
                print(f"✅ Order {order_id} has been cancelled.")
            else:
                print(f"❌ Order {order_id} is already delivered and cannot be cancelled.")
        else:
            print(f"🔍 Order {order_id} not found.")

    def request_return(self):
        order_id = input("🔄 Enter Order ID for return/exchange (e.g., ORD-123): ").strip().upper()
        if not self.validate_order_id(order_id):
            print("⚠️ Invalid Order ID format. Use format ORD-123.")
            return
        if order_id in self.order_db:
            reason = input("📝 Reason for return/exchange: ").strip()
            if len(reason) < 5:
                print("⚠️ Please provide a reason with at least 5 characters.")
                return
            print(f"📨 Return request for Order {order_id} submitted with reason: '{reason}'.")
        else:
            print(f"🔍 Order {order_id} not found.")

    def view_faqs(self):
        print("\n📚 FAQs:")
        faqs = [
            ("How do I track my order?", "Select option 1 and enter your Order ID (e.g., ORD-123)."),
            ("Can I cancel a delivered order?", "No, only orders not yet delivered can be cancelled via option 2."),
            ("What is the return process?", "Use option 3, provide your Order ID and a reason for return.")
        ]
        for q, a in faqs:
            print(f"Q: {q}\nA: {a}\n")

    def submit_feedback(self):
        feedback = input("💬 Enter your feedback (max 200 characters): ").strip()
        if len(feedback) > 200:
            print("⚠️ Feedback too long. Keep it under 200 characters.")
            return
        if feedback:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.feedback_log.append((timestamp, feedback))
            print("🌟 Thank you for your feedback!")
        else:
            print("⚠️ Feedback cannot be empty.")

    def greet_user(self):
        greeting = input("😊 Say something (or just press Enter for a default greeting): ").strip()
        if greeting:
            print(f"🎉 You said: {greeting}! I'm here to make your shopping experience awesome!")
        else:
            print("👋 Hi! Thanks for chatting with ShopSmart Assistant!")

    def view_feedback_history(self):
        if not self.feedback_log:
            print("📜 No feedback submitted yet.")
            return
        print("\n📜 Feedback History:")
        for timestamp, feedback in self.feedback_log:
            print(f"[{timestamp}] {feedback}")

    def run(self):
        print("🚀 ShopSmart Assistant is ready to help!")
        while True:
            self.display_menu()
            choice = input("➡️ Enter your choice (1-8): ").strip()
            if choice == '1':
                self.track_order()
            elif choice == '2':
                self.cancel_order()
            elif choice == '3':
                self.request_return()
            elif choice == '4':
                self.view_faqs()
            elif choice == '5':
                self.submit_feedback()
            elif choice == '6':
                self.greet_user()
            elif choice == '7':
                self.view_feedback_history()
            elif choice == '8':
                print("🙌 Thank you for using ShopSmart Assistant. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please select a number from 1 to 8.")

# Run the chatbot
if __name__ == "__main__":
    chatbot = CustomerChatbot()
    chatbot.run()



# ### Answer 3: Detailed Step-by-Step Explanation of the Enhanced Elementary Chatbot Code with Concepts

# The enhanced **elementary chatbot** code (provided earlier as the first version in response to your request for a complex version) implements a customer interaction application for a fictional e-commerce platform, **ShopSmart Assistant**. It uses a class-based structure, a simulated order database, feedback logging with timestamps, input validation with regular expressions, and additional features like feedback history. Below is a detailed, step-by-step explanation of the code, including key programming concepts like classes, loops, regular expressions, and dictionaries, to help you understand it thoroughly for your AI practical exam.

# ---

# #### Key Programming Concepts Used
# 1. **Classes and Objects**:
#    - A **class** (`CustomerChatbot`) defines a blueprint for the chatbot, encapsulating data (e.g., `order_db`, `feedback_log`) and methods (e.g., `track_order`).
#    - An **object** is an instance of the class, allowing state persistence (e.g., order statuses).
#    - Purpose: Organizes code, maintains state (e.g., orders, feedback), and supports modularity.

# 2. **Loops**:
#    - A `while` loop in the `run` method keeps the chatbot active, repeatedly displaying the menu and processing inputs until the user exits.
#    - Purpose: Enables continuous user interaction.

# 3. **Conditional Statements (`if-elif-else`)**:
#    - Used to handle different user choices (1-8) and validate inputs (e.g., order ID format).
#    - Purpose: Directs program flow based on user input and conditions.

# 4. **Dictionaries**:
#    - The `order_db` dictionary stores order IDs and their statuses (e.g., `{"ORD-123": "Processing"}`).
#    - Purpose: Simulates a database for tracking order states.

# 5. **Lists**:
#    - The `feedback_log` list stores tuples of (timestamp, feedback) to record user feedback.
#    - Purpose: Maintains a history of feedback with timestamps.

# 6. **Regular Expressions (`re`)**:
#    - Used to validate order IDs (e.g., must match `ORD-\d{3}` like `ORD-123`).
#    - Purpose: Ensures strict input format for order IDs.

# 7. **Input/Output**:
#    - `input()` captures user choices, order IDs, and feedback.
#    - `print()` displays menus, responses, and errors.
#    - Purpose: Facilitates user interaction.

# 8. **Datetime**:
#    - The `datetime` module adds timestamps to feedback entries.
#    - Purpose: Enhances feedback logging with time information.

# 9. **Break Statement**:
#    - Exits the main loop when the user selects the exit option.
#    - Purpose: Terminates the chatbot session.

# ---

# #### Code Explanation: Step-by-Step

# ##### 1. **Imports and Class Definition**
# ```python
# import re
# from datetime import datetime

# class CustomerChatbot:
#     def __init__(self):
#         self.order_db = {}  # Simulated order database: {order_id: status}
#         self.feedback_log = []  # Store feedback with timestamps
# ```
# - **Imports**:
#   - `re`: For regular expression-based order ID validation.
#   - `datetime`: For timestamping feedback.
# - **Class `CustomerChatbot`**:
#   - Initializes:
#     - `order_db`: A dictionary to simulate an order database (e.g., `{"ORD-123": "Processing"}`).
#     - `feedback_log`: A list to store feedback as `(timestamp, feedback)` tuples.
# - **Concepts**:
#   - **Classes**: Encapsulates chatbot state and behavior.
#   - **Dictionaries/Lists**: Store persistent data across interactions.
# - **Example**:
#   - After initialization, `self.order_db = {}`, `self.feedback_log = []`.

# **Purpose**: Sets up the chatbot’s state with a simulated database and feedback storage.

# ---

# ##### 2. **Method: `display_menu`**
# ```python
# def display_menu(self):
#     print("\n🌟 Welcome to ShopSmart Assistant 🌟")
#     print("1. Track Order")
#     print("2. Cancel Order")
#     print("3. Request Return/Exchange")
#     print("4. View FAQs")
#     print("5. Submit Feedback")
#     print("6. Chat with a Greeting")
#     print("7. View Feedback History")
#     print("8. Exit")
# ```
# - **Purpose**: Displays the chatbot’s menu with 8 options.
# - **Steps**:
#   - Prints a header and numbered options using emojis for visual appeal.
# - **Concept: Output**:
#   - Uses `print()` to format the menu clearly.
# - **Example Output**:
#   ```
#   🌟 Welcome to ShopSmart Assistant 🌟
#   1. Track Order
#   2. Cancel Order
#   3. Request Return/Exchange
#   4. View FAQs
#   5. Submit Feedback
#   6. Chat with a Greeting
#   7. View Feedback History
#   8. Exit
#   ```

# **Purpose**: Provides a user-friendly interface for selecting actions.

# ---

# ##### 3. **Method: `validate_order_id`**
# ```python
# def validate_order_id(self, order_id):
#     return bool(re.match(r'^ORD-\d{3}$', order_id))
# ```
# - **Purpose**: Validates the format of an order ID using a regular expression.
# - **Steps**:
#   - Uses `re.match` to check if `order_id` matches the pattern `^ORD-\d{3}$`:
#     - `^`: Start of string.
#     - `ORD-`: Literal "ORD-".
#     - `\d{3}`: Exactly 3 digits (0-9).
#     - `$`: End of string.
#   - Returns `True` if valid, `False` otherwise.
# - **Concept: Regular Expressions**:
#   - Ensures strict input format (e.g., `ORD-123` is valid, `ORD-12` or `abc` is not).
# - **Example**:
#   - `validate_order_id("ORD-123")` → `True`
#   - `validate_order_id("ORD-12")` → `False`

# **Purpose**: Enforces a consistent order ID format for tracking, cancellation, and returns.

# ---

# ##### 4. **Method: `track_order`**
# ```python
# def track_order(self):
#     order_id = input("📦 Enter your Order ID (e.g., ORD-123): ").strip().upper()
#     if not self.validate_order_id(order_id):
#         print("⚠️ Invalid Order ID format. Use format ORD-123.")
#         return
#     if order_id in self.order_db:
#         status = self.order_db[order_id]
#         print(f"🚚 Order {order_id} is {status}.")
#     else:
#         print(f"🔍 Order {order_id} not found. Please check the ID.")
#         self.order_db[order_id] = "Processing"  # Simulate adding new order
# ```
# - **Purpose**: Tracks an order’s status using its ID.
# - **Steps**:
#   - Prompts for an order ID, strips whitespace, and converts to uppercase.
#   - Validates the ID using `validate_order_id`.
#   - If valid:
#     - Checks if `order_id` exists in `order_db`.
#     - If found, displays the status (e.g., "Processing").
#     - If not found, adds it to `order_db` with status "Processing" (simulates a new order).
#   - If invalid, shows an error.
# - **Concepts**:
#   - **Dictionary**: `order_db` stores and retrieves order statuses.
#   - **Conditional**: Validates input and checks dictionary membership.
#   - **String Manipulation**: `strip().upper()` normalizes input.
# - **Example**:
#   - Input: "ORD-123" (new order) → Output: `🔍 Order ORD-123 not found. Please check the ID.`; `order_db = {"ORD-123": "Processing"}`
#   - Input: "ORD-123" (again) → Output: `🚚 Order ORD-123 is Processing.`

# **Purpose**: Simulates order tracking with persistent state.

# ---

# ##### 5. **Method: `cancel_order`**
# ```python
# def cancel_order(self):
#     order_id = input("🛑 Enter Order ID to cancel (e.g., ORD-123): ").strip().upper()
#     if not self.validate_order_id(order_id):
#         print("⚠️ Invalid Order ID format. Use format ORD-123.")
#         return
#     if order_id in self.order_db:
#         if self.order_db[order_id] != "Delivered":
#             self.order_db[order_id] = "Cancelled"
#             print(f"✅ Order {order_id} has been cancelled.")
#         else:
#             print(f"❌ Order {order_id} is already delivered and cannot be cancelled.")
#     else:
#         print(f"🔍 Order {order_id} not found.")
# ```
# - **Purpose**: Cancels an order if it’s not delivered.
# - **Steps**:
#   - Prompts for order ID and validates it.
#   - If valid and in `order_db`:
#     - Checks if status is not "Delivered".
#     - If cancellable, updates status to "Cancelled" and confirms.
#     - If delivered, shows an error.
#   - If not found or invalid, shows appropriate errors.
# - **Concepts**:
#   - **Dictionary**: Updates `order_db` with new status.
#   - **Nested Conditionals**: Checks ID validity, existence, and status.
# - **Example**:
#   - Input: "ORD-123" (status: "Processing") → Output: `✅ Order ORD-123 has been cancelled.`; `order_db["ORD-123"] = "Cancelled"`
#   - Input: "ORD-456" (not found) → Output: `🔍 Order ORD-456 not found.`

# **Purpose**: Manages order cancellations with status-based logic.

# ---

# ##### 6. **Method: `request_return`**
# ```python
# def request_return(self):
#     order_id = input("🔄 Enter Order ID for return/exchange (e.g., ORD-123): ").strip().upper()
#     if not self.validate_order_id(order_id):
#         print("⚠️ Invalid Order ID format. Use format ORD-123.")
#         return
#     if order_id in self.order_db:
#         reason = input("📝 Reason for return/exchange: ").strip()
#         if len(reason) < 5:
#             print("⚠️ Please provide a reason with at least 5 characters.")
#             return
#         print(f"📨 Return request for Order {order_id} submitted with reason: '{reason}'.")
#     else:
#         print(f"🔍 Order {order_id} not found.")
# ```
# - **Purpose**: Processes return/exchange requests.
# - **Steps**:
#   - Prompts for order ID and validates it.
#   - If valid and in `order_db`:
#     - Prompts for a reason.
#     - Ensures reason is at least 5 characters.
#     - Confirms the request if valid.
#   - Shows errors for invalid ID, missing order, or short reason.
# - **Concepts**:
#   - **Conditional**: Multi-level validation (ID, order existence, reason length).
#   - **Input Validation**: Ensures meaningful inputs.
# - **Example**:
#   - Input: "ORD-123", "Defective item" → Output: `📨 Return request for Order ORD-123 submitted with reason: 'Defective item'.`
#   - Input: "ORD-123", "Bad" → Output: `⚠️ Please provide a reason with at least 5 characters.`

# **Purpose**: Handles return requests with robust validation.

# ---

# ##### 7. **Method: `view_faqs`**
# ```python
# def view_faqs(self):
#     print("\n📚 FAQs:")
#     faqs = [
#         ("How do I track my order?", "Select option 1 and enter your Order ID (e.g., ORD-123)."),
#         ("Can I cancel a delivered order?", "No, only orders not yet delivered can be cancelled via option 2."),
#         ("What is the return process?", "Use option 3, provide your Order ID and a reason.")
#     ]
#     for q, a in faqs:
#         print(f"Q: {q}\nA: {a}\n")
# ```
# - **Purpose**: Displays a list of FAQs.
# - **Steps**:
#   - Defines a list of tuples `(question, answer)` for FAQs.
#   - Iterates over `faqs` using a `for` loop to print each question and answer.
# - **Concepts**:
#   - **List**: Stores FAQs as structured data.
#   - **Loop**: Iterates to display each FAQ.
# - **Example Output**:
#   ```
#   📚 FAQs:
#   Q: How do I track my order?
#   A: Select option 1 and enter your Order ID (e.g., ORD-123).

#   Q: Can I cancel a delivered order?
#   A: No, only orders not yet delivered can be cancelled via option 2.

#   Q: What is the return process?
#   A: Use option 3, provide your Order ID and a reason.
#   ```

# **Purpose**: Provides quick answers to common queries.

# ---

# ##### 8. **Method: `submit_feedback`**
# ```python
# def submit_feedback(self):
#     feedback = input("💬 Enter your feedback (max 200 characters): ").strip()
#     if len(feedback) > 200:
#         print("⚠️ Feedback too long. Keep it under 200 characters.")
#         return
#     if feedback:
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.feedback_log.append((timestamp, feedback))
#         print("🌟 Thank you for your feedback!")
#     else:
#         print("⚠️ Feedback cannot be empty.")
# ```
# - **Purpose**: Collects and logs user feedback with a timestamp.
# - **Steps**:
#   - Prompts for feedback and checks length (≤200 characters).
#   - If non-empty and valid, records current timestamp and appends `(timestamp, feedback)` to `feedback_log`.
#   - Shows errors for empty or overly long feedback.
# - **Concepts**:
#   - **List**: `feedback_log` stores feedback history.
#   - **Datetime**: `datetime.now().strftime` formats the timestamp (e.g., "2025-05-02 10:30:45").
#   - **Conditional**: Validates feedback length and content.
# - **Example**:
#   - Input: "Great service!" → Output: `🌟 Thank you for your feedback!`; `feedback_log = [("2025-05-02 10:30:45", "Great service!")]`
#   - Input: "" → Output: `⚠️ Feedback cannot be empty.`

# **Purpose**: Gathers and stores feedback for later review.

# ---

# ##### 9. **Method: `greet_user`**
# ```python
# def greet_user(self):
#     greeting = input("😊 Say something (or just press Enter for a default greeting): ").strip()
#     if greeting:
#         print(f"🎉 You said: {greeting}! I'm here to make your shopping experience awesome!")
#     else:
#         print("👋 Hi! Thanks for chatting with ShopSmart Assistant!")
# ```
# - **Purpose**: Engages the user with a customizable greeting.
# - **Steps**:
#   - Prompts for a user message or allows an empty input.
#   - If non-empty, echoes the input in a response.
#   - If empty, shows a default greeting.
# - **Concept: Conditional**:
#   - Uses `if-else` to handle custom vs. default responses.
# - **Example**:
#   - Input: "Hi there" → Output: `🎉 You said: Hi there! I'm here to make your shopping experience awesome!`
#   - Input: "" → Output: `👋 Hi! Thanks for chatting with ShopSmart Assistant!`

# **Purpose**: Adds an interactive, friendly feature.

# ---

# ##### 10. **Method: `view_feedback_history`**
# ```python
# def view_feedback_history(self):
#     if not self.feedback_log:
#         print("📜 No feedback submitted yet.")
#         return
#     print("\n📜 Feedback History:")
#     for timestamp, feedback in self.feedback_log:
#         print(f"[{timestamp}] {feedback}")
# ```
# - **Purpose**: Displays all feedback with timestamps.
# - **Steps**:
#   - Checks if `feedback_log` is empty; if so, shows a message.
#   - Otherwise, iterates over `feedback_log` to print each entry with its timestamp.
# - **Concepts**:
#   - **List**: Iterates over `feedback_log` tuples.
#   - **Loop**: `for` loop displays each feedback entry.
#   - **Conditional**: Handles the empty case.
# - **Example**:
#   - If `feedback_log = [("2025-05-02 10:30:45", "Great service!")]`:
#     ```
#     📜 Feedback History:
#     [2025-05-02 10:30:45] Great service!
#     ```

# **Purpose**: Provides a summary of user feedback.

# ---

# ##### 11. **Method: `run`**
# ```python
# def run(self):
#     print("🚀 ShopSmart Assistant is ready to help!")
#     while True:
#         self.display_menu()
#         choice = input("➡️ Enter your choice (1-8): ").strip()
#         if choice == '1':
#             self.track_order()
#         elif choice == '2':
#             self.cancel_order()
#         elif choice == '3':
#             self.request_return()
#         elif choice == '4':
#             self.view_faqs()
#         elif choice == '5':
#             self.submit_feedback()
#         elif choice == '6':
#             self.greet_user()
#         elif choice == '7':
#             self.view_feedback_history()
#         elif choice == '8':
#             print("🙌 Thank you for using ShopSmart Assistant. Goodbye!")
#             break
#         else:
#             print("⚠️ Invalid choice. Please select a number from 1 to 8.")
# ```
# - **Purpose**: The main loop that drives the chatbot.
# - **Steps**:
#   - Prints a welcome message.
#   - Runs a `while True` loop:
#     - Displays the menu.
#     - Captures user `choice`.
#     - Maps `choice` to methods (1-8) using `if-elif`.
#     - Handles invalid inputs with an error.
#     - Exits on choice '8' with a goodbye message and `break`.
# - **Concepts**:
#   - **Loop**: `while True` ensures continuous operation.
#   - **Conditional**: `if-elif-else` routes choices to methods.
#   - **Break**: Exits the loop on '8'.
# - **Example**:
#   - User enters "1" → Calls `track_order()`.
#   - User enters "8" → Outputs goodbye and exits.

# **Purpose**: Orchestrates user interactions and method calls.

# ---

# ##### 12. **Main Execution**
# ```python
# if __name__ == "__main__":
#     chatbot = CustomerChatbot()
#     chatbot.run()
# ```
# - **Purpose**: Creates a `CustomerChatbot` object and starts the chatbot.
# - **Concept: Program Entry Point**:
#   - Ensures `run()` is called only when the script is executed directly.
# - **Example**:
#   - Instantiates `chatbot` and begins the interaction loop.

# **Purpose**: Initializes and launches the chatbot.

# ---

# ### Execution Walkthrough
# Simulated session:
# 1. **Start**:
#    - Output: `🚀 ShopSmart Assistant is ready to help!` and menu.
# 2. **Track Order**:
#    - Input: "1", "ORD-123".
#    - Output: `🔍 Order ORD-123 not found. Please check the ID.`; `order_db = {"ORD-123": "Processing"}`.
# 3. **Submit Feedback**:
#    - Input: "5", "Great service!".
#    - Output: `🌟 Thank you for your feedback!`; `feedback_log = [("2025-05-02 10:30:45", "Great service!")]`.
# 4. **View Feedback History**:
#    - Input: "7".
#    - Output: `📜 Feedback History: [2025-05-02 10:30:45] Great service!`
# 5. **Exit**:
#    - Input: "8".
#    - Output: `🙌 Thank you for using ShopSmart Assistant. Goodbye!`

# ---

# ### Expected Output
# Running `python3 chatbot.py` in VS Code terminal starts the chatbot. A sample interaction:
# ```
# 🚀 ShopSmart Assistant is ready to help!
# 🌟 Welcome to ShopSmart Assistant 🌟
# 1. Track Order
# 2. Cancel Order
# 3. Request Return/Exchange
# 4. View FAQs
# 5. Submit Feedback
# 6. Chat with a Greeting
# 7. View Feedback History
# 8. Exit
# ➡️ Enter your choice (1-8): 1
# 📦 Enter your Order ID (e.g., ORD-123): ORD-123
# 🔍 Order ORD-123 not found. Please check the ID.
# ...
# ➡️ Enter your choice (1-8): 5
# 💬 Enter your feedback (max 200 characters): Great service!
# 🌟 Thank you for your feedback!
# ...
# ➡️ Enter your choice (1-8): 7
# 📜 Feedback History:
# [2025-05-02 10:30:45] Great service!
# ...
# ➡️ Enter your choice (1-8): 8
# 🙌 Thank you for using ShopSmart Assistant. Goodbye!
# ```

# ---

# ### Notes for Your Exam
# - **Key Concepts**:
#   - **Classes**: `CustomerChatbot` organizes methods and state (`order_db`, `feedback_log`).
#   - **Dictionaries**: `order_db` simulates persistent order tracking.
#   - **Regular Expressions**: `validate_order_id` ensures strict ID formats.
#   - **Loops**: `while True` in `run` enables continuous interaction.
#   - **Datetime**: Timestamps enhance feedback logging.
# - **Code Structure**: Be ready to explain the class, `validate_order_id`, `order_db` usage, and feedback logging.
# - **Edge Cases**:
#   - Invalid order IDs (e.g., "ORD-12") or empty inputs are handled.
#   - Delivered orders can’t be cancelled.
#   - Feedback length is capped at 200 characters.
# - **Running in VS Code**: Save as `chatbot.py`, ensure `python3` works, and run `python3 chatbot.py` in the terminal.
# - **Customization**: Add more options or statuses by extending the menu and methods.

# This explanation, with concepts like classes, loops, and regular expressions, should help you master the enhanced chatbot for your AI practical exam. If you have more practicals or need further clarification, let me know!