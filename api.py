import openai
import os
openai.api_key = "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"
system_message = {
    "role": "system",
    "content": "You are a friendly customer support assistant for BookWorld, an online bookstore specializing in fiction, non-fiction, and academic books. You are here to help customers with their queries regarding books, orders, and services."
}

knowledge_base = {
    "shipping": {
        "keywords": ["shipping", "delivery", "shipment", "deliver"],
        "answer": "Standard shipping within India typically takes 5-7 business days. International shipping times vary by destination. You can find more details on our 'Shipping Information' page."
    },
    "return policy": {
        "keywords": ["return", "refund", "exchange", "policy"],
        "answer": "Our return policy allows you to return books within 30 days of purchase if they are in their original, resalable condition. Please visit our 'Returns & Refunds' page for a detailed guide."
    },
    "contact": {
        "keywords": ["contact", "support", "email", "phone"],
        "answer": "You can reach our customer support team via email at support@bookworld.com or call us at +91-1234567890 during our business hours (Monday-Friday, 9 AM - 6 PM IST)."
    },
    "genres": {
        "keywords": ["genres", "types of books", "categories"],
        "answer": "BookWorld offers a vast selection across fiction (fantasy, sci-fi, romance, thrillers), non-fiction (biographies, history, self-help), and a comprehensive range of academic books (textbooks, research papers). Is there a particular genre you're interested in?"
    },
    "discounts": {
        "keywords": ["discount", "sale", "offer", "promotion", "coupon"],
        "answer": "Keep an eye on our 'Promotions' page for exciting discounts and special offers! We regularly update it with new deals."
    },
    "bookworld_info": {
        "keywords": ["about bookworld", "what is bookworld"],
        "answer": "BookWorld is your premier online destination for a vast selection of books across various genres and academic disciplines, dedicated to providing a seamless shopping experience."
    },
    "hello": {
        "keywords": ["hello", "hi", "hey", "greetings"],
        "answer": "Hi there! Welcome to BookWorld. How can I assist you today?"
    },
    "thank_you": {
        "keywords": ["thanks", "thank you", "much obliged"],
        "answer": "You're most welcome! Is there anything else I can help you with today?"
    }
}

print("Welcome to BookWorld! Type 'exit' to end the chat.\n")
conversation_history = [system_message]
api_key_valid = True

while True:
    user_input = input("You: ")
    user_input_lower = user_input.lower()

    if user_input_lower == "exit":
        print("Chatbot: Thank you for contacting BookWorld. We hope to see you again soon!")
        break
    chatbot_reply = None
    for key, data in knowledge_base.items():
        if any(keyword in user_input_lower for keyword in data["keywords"]):
            chatbot_reply = data["answer"]
            break
    if "order" in user_input_lower and ("status" in user_input_lower or "track" in user_input_lower):
        import re
        order_number_match = re.search(r'(BW\d{5,}|[A-Za-z]{2}\d{5,}|order\s*number\s*is\s*(\w+))', user_input, re.IGNORECASE)
        if order_number_match:
            order_number = order_number_match.group(1) or order_number_match.group(2)
            chatbot_reply = f"Thank you for providing your order number, {order_number}. Please allow a moment while I look up its status for you. (This is a simulated lookup. In a real system, I'd fetch data from our database.)"
        else:
            chatbot_reply = "To track your order, please provide your order number. For example, 'My order number is BW12345'."

    elif "book" in user_input_lower and "recommend" in user_input_lower:
        chatbot_reply = "I'd love to help with book recommendations! What genres are you interested in, or are you looking for something similar to a book you've enjoyed?"

    if chatbot_reply:
        print("Chatbot:", chatbot_reply)
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": chatbot_reply})
        continue 
    if not api_key_valid:
        print("Chatbot: I apologize, but I'm currently unable to connect to my advanced AI. Please try rephrasing your question, or you can check our FAQ section on the BookWorld website for common inquiries.")
        continue
    conversation_history.append({"role": "user", "content": user_input})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history, 
            timeout=15 
        )
        chatbot_reply = response.choices[0].message.content
        api_key_valid = True 

    except openai.APIError as e:
        print(f"Chatbot: (OpenAI API Error) I'm sorry, I'm having trouble connecting to my knowledge base right now. It seems there might be an issue with the service or my API key. Please try again in a few moments. Error: {e}")
        chatbot_reply = "I'm sorry, I'm currently experiencing technical difficulties and cannot provide an advanced response. Please try asking your question differently or refer to our website's FAQ."
        api_key_valid = False 
    except Exception as e:
        print(f"Chatbot: (General Error) An unexpected error occurred: {e}")
        chatbot_reply = "I apologize, but I'm unable to process your request at this moment due to a technical issue. Please try again later."
        api_key_valid = False
    print("Chatbot:", chatbot_reply)
    conversation_history.append({"role": "assistant", "content": chatbot_reply})
