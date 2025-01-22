<h1>Simple random dice simulator <i>2025</i></h1>
<img style= "width:100px" src="https://cdn-icons-png.flaticon.com/512/7101/7101743.png">

The Random Dice Roller is an interactive Python program designed to simulate rolling a dice. It provides a visual ASCII representation of dice faces, making it an engaging way to roll up to 6 dice at a time.

<h2>Features</h2>
<li><b>Roll Multiple Dice:</b> Roll between 1 and 6 dice in a single session.</li>
<li><b>Random Generation:</b> Generates random results using Python's random.randint() function.</li>
<li><b>ASCII Art Display:</b> Visual representation of dice faces with ASCII diagrams.</li>
<li><b>User-Friendly Input:</b> Prompts for user input with validation to ensure accurate results.</li>

<h2>Installation</h2>
<ol>
<li>Ensure Python is installed.</li>
<li>Clone the repository:</li>

    git clone https://github.com/MarianaAa01/Random-dice.git

<li>Navigate to the project directory:</li>
   
    cd Random-dice

</ol>

<h2>Usage</h2>
<ol>
<li><b>Run the application:</b> Execute the script using the command:</li>
   
    python3 diceSimulator.py


<li><b>Follow the prompts:</b> </li></ol>
<ul>
<li>Enter the number of dice you want to roll (between 1 and 6).</li>
<li>View the randomly generated dice results and their corresponding ASCII diagrams.</li>
</ul>


<h2>Code Structure</h2>
<ol>
<li><b>Input Parsing:</b> The parse_input function validates user input to ensure it's an integer between 1 and 6. </li>
<li><b>Random Dice Rolling:</b> The roll_dice function uses the random.randint() method to generate random values for each dice. It creates a list with a length equal to the number of dices specified by the user, populates it with random numbers between 1 and 6, and returns the results for display.</li>
<li><b>ASCII Diagram Generation:</b> The generate_result function constructs ASCII art for dice faces based on the rolled values.</li>
<li><b>Main Execution Block:</b> Combines all steps to provide a seamless user experience.</li>

</ol>
