goals_page_html='''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charSet="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Learn HTMX</title>
    <link rel="stylesheet" href="/static/main_07s18.css" />
    <script src="/static/htmx.js" defer></script>
  </head>
  <body>
    <main>
      <h1>Manage your course goals</h1>
      <section>
        <form id="goal-form">
          <div>
            <label htmlFor="goal">Goal</label>
            <input type="text" id="goal" name="goal" />
          </div>
          <button type="submit">Add goal</button>
        </form>
      </section>
      <section>
        <ul id="goals">
          <li id="goal-1">
            <span>Goal Placeholer</span>
            <button>Remove</button>
          </li>
        </ul>
      </section>
    </main>
  </body>
</html>
'''

goal_list_ul = '''
<ul id="goals">
  <li id="goal-1">
    <span>Goal Placeholer</span>
    <button>Remove</button>
  </li>
</ul>
'''


# NEXT CODE REMOVED FROM HTML
# <section>
#   <ul id="goals">
#   ${courseGoals.map(
#     (goal, index) => `
#     <li id="goal-${index}">
#       <span>${goal}</span>
#       <button>Remove</button>
#     </li>
#   `
#   )}
#   </ul>
# </section>


dum_page_test='''
<!DOCTYPE html>
<html>
  <head>
    <link rel = "stylesheet" type="text/css" href="/static/main.css">
    <link rel="icon" href="/static/icon.png" />
    <title>HTMX Essentials</title>

    <script src="/static/js/htmx.js" defer></script>
  </head>
  <body>
    <header id="main-header">
      <img src="/static/htmx-logo.jpg" alt="HTMX Logo" />
      <h1>Essentials</h1>
    </header>

    <main>
    <div id="testform">
      <p>HTMX is a JavaScript library that you use without writing JavaScript code.</p>
      <form id="testform" hx-post="/formin/">
        <p>
            <label for="note">Your note</label>
            <input type="text" id="note" name="note" required>
        </p>
        <p>
            <button type="submit">Save Note</button>
        </p>
    </form>
    </div>
    </main>
  </body>
</html>
'''

dum_page= '''
<!DOCTYPE html>
<html>
  <head>
    <link rel = "stylesheet" type="text/css" href="/static/main.css">
    <link rel="icon" href="/static/icon.png" />
    <title>HTMX Essentials</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
      rel="stylesheet"

    />
    <!-- <link rel="stylesheet" href="/main.css" /> -->
    <script src="/static/js/htmx.js" defer></script>
  </head>
  <body>
    <header id="main-header">
      <img src="/static/htmx-logo.jpg" alt="HTMX Logo" />
      <h1>Essentials</h1>
    </header>

    <main>
    <div id="testform">
      <p>HTMX is a JavaScript library that you use without writing JavaScript code.</p>
      <!-- HX POST uses value in 'name' as reference id-->
      <form hx-post="/formin" hx-target="#result">
        <p>
            <label for="note">Your note</label>
            <input type="text" id="note" name="note" required>
        </p>
        <p>
            <button type="submit">Save Note</button>
        </p>
      </form>
    </div>
    <div id="result"></div>
<!-- hx-get THIS BUTTON IS MODIFIED WITH HTMLX hx-get attribute -->
      <button hx-get="/info" hx-swap="outerHTML" >Learn More</button>
      <button
      hx-get="/info"
      hx-trigger="mouseenter[ctrlKey],click"
      hx-target="main"
      hx-swap="beforeend" >Learn More</button>
    </main>
  </body>
</html>
'''

HTMX_KNOWLEDGE = [
  'HTMX is a great alternative to React etc.',
  'It offers a different way of loading data into your frontend web UI.',
  'It might be especially interesting for server-side developers who are not so familiar with frontend development.',
  "But - as you will see - it's actually also a very promising alternative to React, Angular etc.",
  'You just have to be open for a diffent mental model.',
  'When using HTMX you typically write way less frontend JavaScript code.',
  "You also don't need to manage any frontend state.",
  'Though you can always add extra JS code if needed.',
  'And you can also combine HTMX with other libraries like AlpineJS or integrate it into React apps etc.',
]

def dummy_page()-> str:
    return dum_page

def goals_page() -> str:
    return goals_page_html

def make_ul(input_list: list[str])->str:
    # create <li> items
    li_elements = [f"<li>{item}</li>" for item in input_list]

    # join items into a single string
    li_string = "".join(li_elements)

    # wrap in <ul> tag
    html_output = f"<ul>{li_string}</ul>"
    return html_output
