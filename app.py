import gradio as gr
from functions import get_dish_list, get_recipe, additional_info

with gr.Blocks() as demo:
    gr.Markdown("# Recipe Suggester")
    gr.Markdown("## Get Personalized Recipe Suggestions and Detailed Recipes")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Enter Your Details")
            groceries = gr.Textbox(label="Available Groceries", placeholder="E.g., tomatoes, onions, chicken, pasta")
            recipe_type = gr.Radio(choices=["Vegetarian", "Non-Vegetarian", "Vegan"], label="Recipe Type")
            cuisine_style = gr.Radio(choices=["Indian", "Italian", "Chinese", "Arabian", "Korean"], label="Cuisine Style")
            allergies = gr.Textbox(label="Allergies", placeholder="E.g., nuts, dairy")
            servings = gr.Number(label="Servings", value=1, precision=0)
            max_time = gr.Number(label="Max Cooking Time (minutes)", value=30, precision=0)
            dish_suggestions_btn = gr.Button("Get Dish Suggestions")
            dish_suggestions_output = gr.Textbox(label="Dish Suggestions", interactive=False)
       
        with gr.Column():
            gr.Markdown("### Recipe Details and Additional Information")
            dish_name = gr.Textbox(label="Dish Name from Suggestions", placeholder="Enter a dish name from the suggestions")
            get_recipe_btn = gr.Button("Get Recipe")
            recipe_output = gr.Textbox(label="Recipe", interactive=False)
            download_recipe_btn = gr.File(label="Download Recipe")
            user_question = gr.Textbox(label="Additional Questions or Requests", placeholder="E.g., Can I substitute ingredient X with Y?")
            additional_suggestions_btn = gr.Button("Get Additional Info")
            additional_suggestions_output = gr.Textbox(label="Additional Information", interactive=False)
            download_additional_info_btn = gr.File(label="Download Additional Information")

    dish_suggestions_btn.click(get_dish_list,
                               [groceries, recipe_type, cuisine_style, allergies, servings, max_time],
                               dish_suggestions_output)
    get_recipe_btn.click(get_recipe,
                         [dish_name, groceries, recipe_type, cuisine_style, allergies, servings, max_time],
                         [recipe_output, download_recipe_btn])
    additional_suggestions_btn.click(additional_info,
                                     [user_question],
                                     [additional_suggestions_output, download_additional_info_btn])

demo.launch()





