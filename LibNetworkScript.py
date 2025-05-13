import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from itertools import combinations
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output, State
import dash


# ------------- DATA SET -------------
title = ['Feeling at Home: Transforming the Politics of Housing',
'They Call It Love:The Politics of Emotional Life',
'Everything to Play For:How Videogames Are Changing the World',
'Exile and Pride',
'Lab Girl',
'The Noonday Demon',
'Entangled Life',
'Capitalist Realism',
'How Forests Think: Toward an Anthropology Beyond the Human',
'A Field Guide to Getting Lost',
'Atlas of AI',
'Autism Is Not A Disease:The Politics of Neurodiversity',
'Microbiopolitics of Milk',
'What’s Love (or Care, Intimacy, Warmth, Affection) Got to Do with It?',
'The Story of More',
'All About Love: New Visions',
'On Women',
'Staying with the Trouble',
'The Eye of the Master: A Social History of Artificial Intelligence',
'Blue Machine: How the Ocean Shapes Our World',
'The Light Eaters: How the Unseen World of Plant Intelligence Offers a New Understanding of Life on Earth',
'Recollections of My Nonexistence',
'The egg and the chicken',
'The Carrier Bag Theory of Fiction',
'A Cyborg Manifesto',
'Against the Anthropocene',
'Matter Fictions',
'Theater, Garden, Bestiary: A Materialist History of Exhibitions',
'Cyberboss:The Rise of Algorithmic Management and the New Struggle for Control at Work']


author = ['Gotby Alva',
'Gotby Alva',
'Did Marijam',
'Clare Eli',
'Jahren Hope',
'Solomon Andrew',
'Sheldrake Merlin',
'Fisher Mark',
'Kohn Eduardo',
'Solnit Rebecca',
'Crawford Kate',
'Hare Jodie',
'Despret V., Fite-Wassilak C., Garcia-Dory F., Jackson M., Leslie E., Nimmo R., Paxson H., West H. G.',
'Chan P., Chukhrov K., Cluster, Povinelli, E. A. and Turcot Difruscia K., Engel A., Fang H., Moten F. and Harney S., Mackinnon L., Martinez C., Meraud T., Preciado P. B., Rosler M., Solomon V., Toufic J., Verwoert J., Kuan Wood B., Žizek S.',
'Jahren Hope',
'Hooks Bell',
'Sontag Susan',
'Haraway Donna J.',
'Pasquinelli Matteo',
'Czerski Helen',
'Schlanger Zoë',
'Solnit Rebecca',
'Lispector Clarice',
'Le Guin Ursula K.',
'Haraway Donna J.',
'Demos T. J.',
'Biermann U., CCRU, Eshun K., Hayles N. K.N., Mackee F., Mendes M., Parikka J., Silva M., Teets J., Waite J.',
'Garcia Tristan, Normand Vincent',
'Gent Craig']

year = [2025,
2023,
2024,
1999,
2017,
2001,
2020,
2009,
2013,
2006,
2021,
2024,
2023,
2017,
2020,
1999,
2023,
2016,
2023,
2024,
2024,
2020,
1960,
1986,
1985,
2017,
2017,
2019,
2024]

main_theme = ['Social reproduction',
'Social reproduction',
'Social reproduction',
'LGBTQ',
'Biology',
'Mental Illness',
'Ecology',
'Capitalism',
'Ecology',
'Feminism',
'Technology',
'Social reproduction',
'Biology',
'Emotion',
'Ecology',
'Social reproduction',
'Feminism',
'Feminism',
'Social reproduction',
'Biology',
'Biology',
'Housing',
'Complexity',
'Technology',
'Complexity',
'Complexity',
'Complexity',
'Technology',
'Technology']

theme = [['Housing'],
['Emotion, Feminism'],
['Technology'],
['Feminism'],
['Emotion'],
['Emotion, Complexity'],
['Biology, Emotion, Capitalism'],
['Mental Illness'],
['Emotion'],
['Housing'],
['Capitalism'],
['Capitalism'],
['Technology, Capitalism'],
['Social reproduction, Capitalism'],
['Biology, Technology, Capitalism'],
['Feminism, Emotion, Capitalism'],
['Social reproduction'],
['Ecology, Technology, Emotion'],
['Technology, Capitalism'],
['Ecology, Complexity'],
['Ecology, Technology, Emotion'],
['Feminism, Emotion'],
['Feminism'],
['Emotion, Feminism'],
['Technology, Feminism'],
['Technology, Ecology'],
['Technology, Ecology'],
['Social reproduction'],
['Social reproduction']]

summary = ["Feeling at Home grapples with the practical and emotional questions of housing – domestic labour, privacy, security, ownership, and health. Is it possible to imagine success without home ownership? Alva Gotby makes clear that solving the housing crisis is about much more than housing stock. It is about revolutionising our everyday lives and labours.",
"They Call It Love investigates the work that makes a haven in a heartless world, examining who performs this labour, how it is organised, and how it might change. Drawing on the thought of the feminist movement Wages for Housework, Gotby demonstrates that emotion is a key element in the reproduction of society and its norms. Addressing the problem of love's labour requires nothing less than a radical restructuring of society.",
"The videogame industry, now larger than the film and music industries combined, has a proven ability to challenge the status quo. With a rich array of examples, Did argues for a nuanced understanding of gaming’s influence so that this extraordinary power can be harnessed for good.",
"His essays weave together memoir, history, and political thinking to explore meanings and experiences of home: home as place, community, bodies, identity, and activism. Here readers will find an intersectional framework for understanding how we actually live with the daily hydraulics of oppression, power, and resistance.",
"Lab Girl is a book about work and about love, and the mountains that can be moved when those two things come together. It is told through Jahren's remarkable stories: about the discoveries she has made in her lab, as well as her struggle to get there; about her childhood playing in her father's laboratory; about how lab work became a sanctuary for both her heart and her hands; about Bill, the brilliant, wounded man who became her loyal colleague and best friend; about their field trips - sometimes authorised, sometimes very much not - that took them from the Midwest across the USA, to Norway and to Ireland, from the pale skies of North Pole to tropical Hawaii; and about her constant striving to do and be her best, and her unswerving dedication to her life's work.",
"The Noonday Demon’s contribution to our understanding not only of mental illness but also of the human condition in general is stunning. The book examines depression in personal, cultural, and scientific terms. Drawing on his own struggles with the illness and interviews with fellow sufferers, doctors and scientists, policymakers and politicians, drug designers and philosophers, Solomon reveals the subtleties, the complexities, and the agony of the disease.",
"Fungi throw our concepts of individuality and even intelligence into question. They can change our minds, heal our bodies, and even help us remediate environmental disaster. By examining fungi on their own terms, Sheldrake reveals how these extraordinary organisms – and our relationships with them – are changing our understanding of how life works.",
"After 1989, capitalism has successfully presented itself as the only realistic political-economic system - a situation that the bank crisis of 2008, far from ending, actually compounded. This book analyses the development and principal features of this capitalist realism as a lived ideological framework.",
"Based on four years of fieldwork among the Runa of Ecuador’s Upper Amazon, Eduardo Kohn draws on his rich ethnography to explore how Amazonians interact with the many creatures that inhabit one of the world’s most complex ecosystems. Whether or not we recognize it, our anthropological tools hinge on those capacities that make us distinctly human. However, when we turn our ethnographic attention to how we relate to other kinds of beings, these tools (which have the effect of divorcing us from the rest of the world) break down. How Forests Think seizes on this breakdown as an opportunity. Avoiding reductionistic solutions, and without losing sight of how our lives and those of others are caught up in the moral webs we humans spin, this book skillfully fashions new kinds of conceptual tools from the strange and unexpected properties of the living world itself.",
"Written as a series of autobiographical essays, A Field Guide to Getting Lost draws on emblematic moments and relationships in Rebecca Solnit's life to explore issues of uncertainty, trust, loss, memory, desire, and place. Solnit is interested in the stories we use to navigate our way through the world, and the places we traverse, from wilderness to cities, in finding ourselves, or losing ourselves. While deeply personal, her own stories link up to larger stories, from captivity narratives of early Americans to the use of the color blue in Renaissance painting, not to mention encounters with tortoises, monks, punk rockers, mountains, deserts, and the movie Vertigo.",
"In Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence Crawford reveals how the global networks underpinning AI technology are damaging the environment, entrenching inequality, and fueling a shift toward undemocratic governance. She takes us on a journey through the mining sites, factories, and vast data collections needed to make AI ""work"" — powerfully revealing where they are failing us and what should be done.",
"Jodie Hare, diagnosed with autism at twenty-three, argues it is time to redefine the politics of who we are. She calls for the recognition of diversity as part of natural variation, rather than a departure from sameness. This will have an impact on the places where we learn, work, and socialise - and Hare shows how these can be adapted to be more inclusive and accessible. She shows how we might commit to building a world where we can all thrive, one that works to combat discrimination based on race, class, gender, and disability.",
"In the context of INLAND’s Academy at documenta fifteen, Microbiopolitics of Milk presents the grounding basis for a research project around Milk as a bio-cultural substance, through its implications in the regimes of contemporary biopolitics, economics and representation.",
"In our present times—post-human, post-reality, or maybe pre-internet, post-it, pre-collapse, pre-fabricated by algorithms—what does love have to do with it? Since 2009, need and care and desire and admiration have been cross-examined, called as witness, put on parole, and made the subject of caring inquiry by e-flux journal authors.",
"In The Story of More, she illuminates the link between human habits and our imperiled planet. In concise, highly readable chapters, she takes us through the science behind the key inventions—from electric power to large-scale farming to automobiles—that, even as they help us, release greenhouse gases into the atmosphere like never before. She explains the current and projected consequences of global warming—from superstorms to rising sea levels—and the actions that we all can take to fight back.",
"All About Love reveals what causes a polarized society, and how to heal the divisions that cause suffering. Here is the truth about love, and inspiration to help us instill caring, compassion, and strength in our homes, schools, and workplaces.",
"On Women presents seven essays and exchanges, spanning a range of subjects: the challenges and humiliations women face as they age; the relationship between women’s liberation and class struggle; beauty, which Sontag calls “that over-rich brew of so many familiar opposites”; feminism; fascism; and film.",
"In the midst of spiraling ecological devastation, multispecies feminist theorist Donna J. Haraway offers provocative new ways to reconfigure our relations to the earth and all its inhabitants. She eschews referring to our current epoch as the Anthropocene, preferring to conceptualize it as what she calls the Chthulucene, as it more aptly and fully describes our epoch as one in which the human and nonhuman are inextricably linked in tentacular practices.",
"The Eye of the Master argues, to the contrary, that the inner code of AI is shaped not by the imitation of biological intelligence, but the intelligence of labour and social relations, as it is found in Babbage's ""calculating engines"" of the industrial age as well as in the recent algorithms for image recognition and surveillance.",
"In a book that will re-calibrate our view of this defining feature of our planet, physicist Helen Czerski dives deep to illuminate the murky depths of the ocean engine, examining the messengers, passengers and voyagers that live in it, travel over it, and survive because of it. From the Ancient Polynesians who navigated the Pacific by reading the waves, to permanent residents of the deep like the Greenland shark that can live for hundreds of years, she explains by way of vast currents, invisible ocean walls and underwater waterfalls how all have their place in the oceans' complex interlinked system.",
"It takes tremendous biological creativity to be a plant. To survive and thrive while rooted in a single spot, plants have adapted ingenious methods of survival. In recent years, scientists have learned about their ability to communicate, recognize their kin and behave socially, hear sounds, morph their bodies to blend into their surroundings, store useful memories that inform their life cycle, and trick animals into behaving to their benefit, to name just a few remarkable talents.",
"In Recollections of My Nonexistence, Rebecca Solnit describes her formation as a writer and as a feminist in 1980s San Francisco, in an atmosphere of gender violence on the street and throughout society and the exclusion of women from cultural arenas. She tells of being poor, hopeful, and adrift in the city that became her great teacher, and of the small apartment that, when she was nineteen, became the home in which she transformed herself. She explores the forces that liberated her as a person and as a writer--books themselves; the gay community that presented a new model of what else gender, family, and joy could mean; and her eventual arrival in the spacious landscapes and overlooked conflicts of the American West.",
"“I pick up another egg in the kitchen, I break its shell and shape. And from this precise moment there was never an egg.”",
"In The Carrier Bag Theory of Fiction, visionary author Ursula K. Le Guin retells the story of human origin by redefining technology as a cultural carrier bag rather than a weapon of domination. Hacking the linear, progressive mode of the Techno-Heroic, the Carrier Bag Theory of human evolution proposes: 'before the tool that forces energy outward, we made the tool that brings energy home.' Prior to the preeminence of sticks, swords and the Hero's long, hard, killing tools, our ancestors' greatest invention was the container: the basket of wild oats, the medicine bundle, the net made of your own hair, the home, the shrine, the place that contains whatever is sacred. The recipient, the holder, the story. The bag of stars.",
"In it, the concept of the cyborg represents a rejection of rigid boundaries, notably those separating ""human"" from ""animal"" and ""human"" from ""machine."" The ""Manifesto"" challenges traditional notions of feminism, particularly feminism that focuses on identity politics, and instead encourages coalition through affinity. Haraway uses the concept of a cyborg to represent the plasticity of identity and to highlight the limitations of socially imposed identities; the ""Manifesto"" is considered a major milestone in the development of feminist posthumanist theory.",
"Addressing the current upswing of attention in the sciences, arts, and humanities to the new proposal that we are in a human-driven epoch called the Anthropocene, this book critically surveys that thesis and points to its limitations. It analyzes contemporary visual culture—popular science websites, remote sensing and SatNav imagery, eco-activist mobilizations, and experimental artistic projects—to consider how the term proposes more than merely a description of objective geological periodization. This book argues that the Anthropocene terminology works ideologically in support of a neoliberal financialization of nature, anthropocentric political economy, and endorsement of geoengineering as the preferred—but likely disastrous—method of approaching climate change. To democratize decisions about the world’s near future, we urgently need to subject the Anthropocene thesis to critical scrutiny and develop creative alternatives in the present.",
"Matter Fictions addresses fiction as a mode of producing reality as well as the significance of matter—animal, vegetable, mineral, hybrid—beyond binaries. Recounting a partial history of our relation with matter, the eponymous exhibition at Museu Coleção Berardo (May 4–August 21, 2016) explored how the crossover between cosmological narratives, spatial revolutions of concrete poetry, and hypertextual and territorial fictions might impact our understanding of human agency in a time that calls for action on climate change and technocratic policies. This companion reader features contributions from participating artists and like-minded writers that address the scope of this project as it exceeds the frame of art and the exhibition into the realm of nonhuman ecologies, ontologies, and temporalities.",
"This volume both gathers and expands on the results of the research project “Theater, Garden, Bestiary: A Materialist History of Exhibitions” held at ECAL/University of Art and Design Lausanne, and proposes to draft a history of exhibitions sourced from a wide corpus reaching beyond the framework of art institutions. It undertakes a transdisciplinary history, at the nexus of art history, science studies, and philosophy, exploring the role the exhibition played in the construction of the conceptual categories of modernity, and outlines a historiographical model that grasps the exhibition as both an aesthetic and epistemic site.",
"In Cyberboss, Craig Gent takes us into workplaces where algorithms rule to excavate the politics behind the newest form of managerial power. Combining worker testimony and original research on companies such as Amazon, Uber, and Deliveroo, the cutting edge of algorithmic management technology, this book reveals the sometimes unexpected effects these new techniques have on work, workers and managers. Gent advances an alternative politics of resistance in the face of digital control."]


# ---------- DATAFRAME ----------
df = pd.DataFrame({'Title': title,
                   'Author': author,
                   'Year': year,
                   'Main Theme': main_theme,
                   'Theme': theme,
                   'Summary': summary})


# ---------- Preprocessing ----------
df['Theme'] = df['Theme'].apply(
    lambda lst: lst[0].split(', ') if isinstance(lst, list) and len(lst) == 1 and isinstance(lst[0], str) else lst
)
df_copy = df.copy()
df_exploded = df_copy.explode('Theme')

# ---------- Build Edge List ----------
edge_theme_dict = {}
for theme, group in df_exploded.groupby('Theme'):
    books = group['Title'].unique()
    if len(books) > 1:
        for pair in combinations(books, 2):
            edge = tuple(sorted(pair))
            edge_theme_dict.setdefault(edge, []).append(theme)

edges = list(edge_theme_dict.keys())
unique_themes = df_exploded['Theme'].unique()
theme_colors = {theme: mcolors.rgb2hex(cm.tab20(i / len(unique_themes))) for i, theme in enumerate(unique_themes)}

# ---------- Build Graph ----------
G = nx.Graph()
G.add_nodes_from(df_copy['Title'])
G.add_edges_from(edges)
for _, row in df_copy.iterrows():
    G.nodes[row['Title']].update({
        'Author': row['Author'],
        'Year': row['Year'],
        'Main Theme': row['Main Theme'],
        'Themes': ', '.join(row['Theme'])
    })

# ---------- Position Nodes ----------
authors_sorted = sorted(df_copy['Author'].unique())
themes_sorted = sorted(df_copy['Main Theme'].unique())
author_y = {author: i for i, author in enumerate(authors_sorted)}
theme_x = {theme: i for i, theme in enumerate(themes_sorted)}

x_spacing = 6.5
y_spacing = 1.1
pos = {
    row['Title']: (
        theme_x[row['Main Theme']] * x_spacing,
        author_y[row['Author']] * y_spacing
    )
    for _, row in df_copy.iterrows()
}

# ---------- Build Edge Traces ----------
def build_edge_traces(selected_node=None, selected_theme=None):
    edge_traces = []
    highlight_edges = set()

    # Gather edges to highlight from selected node
    if selected_node:
        for edge in edge_theme_dict:
            if selected_node in edge:
                highlight_edges.add(edge)

    for edge, themes in edge_theme_dict.items():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        num_points = 20
        t = np.linspace(0, 1, num_points)
        xs = x0 + (x1 - x0) * t
        ys = y0 + (y1 - y0) * t

        dx, dy = x1 - x0, y1 - y0
        length = np.hypot(dx, dy)
        if length == 0:
            continue

        norm = np.array([-dy, dx]) / length
        offsets = np.sin(np.pi * t) * 5
        xs += norm[0] * offsets
        ys += norm[1] * offsets

        color = theme_colors.get(themes[0], '#888')
        opacity = 1.0
        width = 0.5

        # Should this edge be highlighted?
        is_highlighted_by_theme = selected_theme and selected_theme in themes
        is_highlighted_by_node = edge in highlight_edges

        if is_highlighted_by_theme or is_highlighted_by_node:
            width = 2
            rgb = mcolors.to_rgb(color)
            brighter_rgb = tuple(min(1, c + 0.3) for c in rgb)
            color = mcolors.to_hex(brighter_rgb)
        elif selected_theme or selected_node:
            opacity = 0.1

        edge_traces.append(go.Scatter(
            x=xs.tolist(),
            y=ys.tolist(),
            line=dict(width=width, color=color),
            hoverinfo='text',
            text=f"<b>Common Theme:</b> {', '.join(themes)}",
            mode='lines',
            customdata=[edge for _ in range(num_points)],
            opacity=opacity,
            name=','.join(themes)
        ))

    return edge_traces



# ---------- Build Node Trace ----------
def build_node_trace(selected_node=None):
    node_x, node_y, node_text = [], [], []
    node_opacity, node_colors, node_sizes = [], [], []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        data = G.nodes[node]
        node_text.append(
            f"<span style='font-size:18px; font-weight:bold; font-style:italic;'>{node}</span><br>{data['Author']}<br>{data['Year']}<br>"
            f"<b>Primary Theme:</b> {data['Main Theme']}<br><b>Secondary Theme:</b> {data['Themes']}"
        )

        if selected_node is None:
            node_opacity.append(1.0)
            node_colors.append('cornflowerblue')
            node_sizes.append(36)
        elif node == selected_node:
            node_opacity.append(1.0)
            node_colors.append('deepskyblue')  # highlighted main node
            node_sizes.append(36)
        elif G.has_edge(selected_node, node) or any(
            edge for edge in edge_theme_dict if selected_node in edge and node in edge
        ):
            node_opacity.append(1.0)
            node_colors.append('lightskyblue')  # connected nodes
            node_sizes.append(24)
        else:
            node_opacity.append(0.2)
            node_colors.append('gray')  # unrelated nodes faded
            node_sizes.append(14)

    return go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[node for node in G.nodes()],
        textposition="top center",
        hoverinfo='text',
        hovertext=node_text,
        marker=dict(
            showscale=False,
            color=node_colors,
            size=node_sizes,
            opacity=0,
            line_width=1
        ),
        textfont=dict(size=9, color='rgba(0,0,0,0)')
    )


# ---------- Layout Settings ----------
x_vals = [x for x, _ in pos.values()]
y_vals = [y for _, y in pos.values()]
x_min, x_max = min(x_vals), max(x_vals)
y_min, y_max = min(y_vals), max(y_vals)
x_margin, y_margin = 1, 1
vertical_lines = [
    dict(
        type="line",
        x0=val * x_spacing, x1=val * x_spacing,
        y0=y_min - y_margin, y1=y_max + y_margin,
        line=dict(color="black", width=0.5, dash="solid"),
        layer='below'
    )
    for val in theme_x.values()
]

# ---------- App and Callbacks ----------
app = Dash(__name__)
app.layout = html.Div([
    html.H2("Rootstalk Library", style={'fontSize': '32px', 'textAlign': 'center', 'color': 'black', 'fontWeight': 'bold'}),
    html.Button("Reset View", id='reset-btn', style={'marginBottom': '10px'}),

    # Store selection & hover state
    dcc.Store(id='selected-node'),
    dcc.Store(id='selected-theme'),
    dcc.Store(id='hovered-node'),

    dcc.Graph(id='network-graph', config={'scrollZoom': True, 'displayModeBar': True}),
], style={'backgroundColor': 'white', 'padding': '20px'})

@app.callback(
    Output('selected-node', 'data'),
    Output('selected-theme', 'data'),
    Input('network-graph', 'clickData'),
    Input('reset-btn', 'n_clicks'),
    State('network-graph', 'figure'),
    prevent_initial_call=True
)
def update_selection(clickData, reset_clicks, prev_figure):
    ctx = dash.callback_context
    trigger = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    if trigger == 'reset-btn':
        return None, None

    if clickData and 'points' in clickData:
        point_data = clickData['points'][0]
        custom = point_data.get('customdata')
        text = point_data.get('text')

        if custom and isinstance(custom, list) and len(custom) == 2:
            curve_index = point_data.get('curveNumber')
            if prev_figure and 'data' in prev_figure and len(prev_figure['data']) > curve_index:
                trace = prev_figure['data'][curve_index]
                return None, trace.get('name')
        elif text in G.nodes:
            return text, None

    return None, None


@app.callback(
    Output('hovered-node', 'data'),
    Input('network-graph', 'hoverData'),
    Input('reset-btn', 'n_clicks'),
    prevent_initial_call=True
)
def update_hover(hoverData, reset_clicks):
    ctx = dash.callback_context
    trigger = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    if trigger == 'reset-btn':
        return None

    if hoverData and 'points' in hoverData:
        text = hoverData['points'][0].get('text')
        if text in G.nodes:
            return text

    return None




@app.callback(
    Output('network-graph', 'figure'),
    Input('selected-node', 'data'),
    Input('selected-theme', 'data'),
    Input('hovered-node', 'data')
)
def update_graph(selected_node, selected_theme, hovered_node):
    edge_traces = build_edge_traces(selected_node, selected_theme)
    node_trace = build_node_trace(selected_node)

    fig = go.Figure(data=edge_traces + [node_trace])
    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=20, r=20, t=40),
        width=1480,
        height=600,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black'),
        xaxis=dict(
            showgrid=False, zeroline=False, showticklabels=True,
            tickvals=[i * x_spacing for i in theme_x.values()],
            ticktext=list(theme_x.keys()),
            range=[x_min - x_margin, x_max + x_margin],
            scaleanchor='y', scaleratio=1,
            side="top",
            tickfont=dict(size=16, family="Times New Roman", weight=750)
        ),
        yaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[y_min - y_margin, y_max + y_margin]
        ),
        shapes=vertical_lines
    )


    # Custom icons
    icon_map = {
        "Feeling at Home: Transforming the Politics of Housing": "/assets/icon/Feeling at Home_Transforming the Politics of Housing.png",
        'They Call It Love:The Politics of Emotional Life': "/assets/icon/They Call It Love_The Politics of Emotional Life.png",
        'Everything to Play For:How Videogames Are Changing the World': "/assets/icon/Everything to Play For_How Videogames Are Changing the World.png",
        'Exile and Pride': "/assets/icon/Exile and Pride.png",
        'Lab Girl': "/assets/icon/Lab Girl.png",
        'The Noonday Demon': "/assets/icon/The Noonday Demon.png",
        'Entangled Life': "/assets/icon/Entangled Life.png",
        'Capitalist Realism': "/assets/icon/Capitalist Realism.png",
        'How Forests Think: Toward an Anthropology Beyond the Human': "/assets/icon/How Forests Think_Toward an Anthropology Beyond the Human.png",
        'A Field Guide to Getting Lost': "/assets/icon/A Field Guide to Getting Lost.png",
        'Atlas of AI': "/assets/icon/Atlas of AI.png",
        'Autism Is Not A Disease:The Politics of Neurodiversity': "/assets/icon/Autism Is Not A Disease_The Politics of Neurodiversity.png",
        'Microbiopolitics of Milk': "/assets/icon/Microbiopolitics of Milk.png",
        'What’s Love (or Care, Intimacy, Warmth, Affection) Got to Do with It?': "/assets/icon/What_s Love.png",
        'The Story of More': "/assets/icon/The Story of More.png",
        'All About Love: New Visions': "/assets/icon/All About Love_New Visions.png",
        'On Women': "/assets/icon/On Women.png",
        'Staying with the Trouble': "/assets/icon/Staying with the Trouble.png",
        'The Eye of the Master: A Social History of Artificial Intelligence': "/assets/icon/The Eye of the Master_A Social History of Artificial Intelligence.png",
        'Blue Machine: How the Ocean Shapes Our World': "/assets/icon/Blue Machine_How the Ocean Shapes Our World.png",
        'The Light Eaters: How the Unseen World of Plant Intelligence Offers a New Understanding of Life on Earth': "/assets/icon/The Light Eaters_How the Unseen World of Plant Intelligence Offers a New Understanding of Life on Earth.png",
        'Recollections of My Nonexistence': "/assets/icon/Recollections of My Nonexistence.png",
        'The egg and the chicken': "/assets/icon/The egg and the chicken.png",
        'The Carrier Bag Theory of Fiction': "/assets/icon/The Carrier Bag Theory of Fiction.png",
        'A Cyborg Manifesto': "/assets/icon/A Cyborg Manifesto.png",
        'Against the Anthropocene': "/assets/icon/Against the Anthropocene.png",
        'Matter Fictions': "/assets/icon/Matter Fictions.png",
        'Theater, Garden, Bestiary: A Materialist History of Exhibitions': "/assets/icon/Theater, Garden, Bestiary_A Materialist History of Exhibitions.png",
        'Cyberboss:The Rise of Algorithmic Management and the New Struggle for Control at Work': "/assets/icon/Cyberboss_The Rise of Algorithmic Management and the New Struggle for Control at Work.png"
    }


    # Add custom icons for nodes
    images = []

    for node, (x, y) in pos.items():
        if node == hovered_node:
            size = 6  # Larger on hover
        elif node == selected_node:
            size = 6  # Highlighted selected node
        elif selected_node and G.has_edge(selected_node, node):
            size = 4.5  # Connected to selected node
        elif selected_node:
            size = 2.5  # Faded / unrelated
        else:
            size = 4  # Default

        images.append(
            dict(
                source=icon_map[node],
                xref="x",
                yref="y",
                x=x,
                y=y,
                sizex=size,
                sizey=size,
                xanchor="center",
                yanchor="middle",
                layer="above"
            )
        )

    fig.update_layout(images=images)

    return fig

# if __name__ == '__main__':
#     app.run(debug=True)


import os
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
