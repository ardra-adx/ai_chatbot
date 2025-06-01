# ai_chatbot
 Chatbot that combines a lightweight rule‑based knowledge base with OpenAI’s GPT models to answer customer queries for BookWorld, an online bookstore.

*The chatbot uses keywords to quickly respond without calling GPT, saving API cost and latency.
#tech used:
python
openai api
Regex-For basic entity extraction
dotenv

-Order Support: Recognizes and responds to order tracking queries.
-Book Recommendations: Responds to genre or book recommendation requests.
-Keyword Matching: Matches specific keywords to deliver pre-defined answers quickly.
-LLM Fallback: Falls back to GPT when no rules are matched.
-API Key Management: Supports both hardcoded keys (not recommended) and .env file support (recommended).

as we used nlp it is used to extract the keywords so we get easy reply from chatbot
in realtime chatbot token cost is charged(api) but here as we use keywords we get the output easily where the questions are similar to the keywords
there are prebuilt output but each time when it goes to gpt is cost tokens
but here only at time where the keywords mismatch they fetch the data from gpt at that time only api key is required

Flow:
-User input is first checked against a rule-based knowledge_base.
-If a match is found (e.g., keyword: shipping), a pre-written response is returned.
-If not, the input is appended to a conversation history and passed to the OpenAI API to generate a smart reply.
-Order number detection is simulated using regular expressions for formats like BW12345.










![Screenshot from 2025-06-01 17-22-41](https://github.com/user-attachments/assets/9f27bab6-3234-45b5-980b-6a49f270b5a9)
