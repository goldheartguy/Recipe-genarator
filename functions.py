import os
from groq import Groq
from fpdf import FPDF

def get_dish_suggestions(client, groceries, recipe_type, cuisine_style, allergies, servings, max_time):
    prompt = f'''These are the available groceries with me: {groceries}.
                 I would like a {recipe_type} recipe.
                 Please suggest 10 dish names from {cuisine_style} cuisine.
                 I have the following allergies: {allergies}.
                 The dishes should serve {servings} people.
                 I have a maximum of {max_time} minutes available for cooking.'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)

def get_recipe_for_dish(client, dish_name, groceries, recipe_type, cuisine_style, allergies, servings, max_time):
    prompt = f'''These are the available groceries with me: {groceries}.
                 I would like a {recipe_type} recipe.
                 Please provide a detailed recipe for {dish_name} from {cuisine_style} cuisine.
                 I have the following allergies: {allergies}.
                 The recipe should serve {servings} people.
                 I have a maximum of {max_time} minutes available for cooking.'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content

def get_additional_suggestions(client, user_question):
    prompt = f'''I need additional suggestions or clarifications regarding the recipe.
                 {user_question}'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content

def get_dish_list(groceries, recipe_type, cuisine_style, allergies, servings, max_time):
    client = Groq(api_key="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")
    return get_dish_suggestions(client, groceries, recipe_type, cuisine_style, allergies, servings, max_time)

def get_recipe(dish_name, groceries, recipe_type, cuisine_style, allergies, servings, max_time):
    client = Groq(api_key="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")
    recipe = get_recipe_for_dish(client, dish_name, groceries, recipe_type, cuisine_style, allergies, servings, max_time)
    recipe_file = f"recipe_{dish_name.replace(' ', '_')}.pdf"
    create_pdf(recipe, recipe_file)
    return recipe, recipe_file

def additional_info(user_question):
    client = Groq(api_key="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")
    additional_info = get_additional_suggestions(client, user_question)
    info_file = "additional_info.pdf"
    create_pdf(additional_info, info_file)
    return additional_info, info_file