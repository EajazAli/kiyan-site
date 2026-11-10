"""Kiyan website: English copy. Arabic lives in content_ar.py with the same names.
Team members live in data/team.json. Figures are quoted exactly from the Kiyan
Demand Space deck (v6). Run `python3 build.py` after any change.
"""

LANG, DIR, OG_LOCALE = "en", "ltr", "en_GB"

SITE = {
    "name": "Kiyan",
    "url": "https://kiyan.sa",
    "tagline": "Where intelligence meets execution.",
    "description": "Kiyan is a Riyadh-based category management and retail execution consultancy. It takes strategy from the boardroom to the shelf through six pillars: Right Reach, Right Category, Right Range, Right Store, Right Space and Right Execution.",
    "footer": "An independent category management and retail execution partner for manufacturers and retailers.",
    "email": "info@kiyan.sa",
    "whatsapp": "966541373036",
    "whatsapp_display": "+966 54 137 3036",
    "linkedin": "https://www.linkedin.com/company/kiyansa",
    "offices": ["Riyadh", "Istanbul", "Cairo"],
}

# Every piece of interface text. Keys are shared with content_ar.py.
UI = {
    "skip": "Skip to content", "home": "Home", "menu": "Menu", "close": "Close",
    "nav_pillars": "Pillars", "nav_how": "How we work", "nav_team": "Team", "nav_faq": "FAQ", "nav_contact": "Contact",
    "lang_switch": "العربية", "lang_switch_label": "عرض الموقع بالعربية",
    "cta_poc": "Start a free POC", "cta_call": "Book a discovery call", "cta_rfp": "Submit your RFP",
    "search": "Search", "search_label": "Search the site", "search_ph": "Search pillars, solutions, people…",
    "theme": "Switch between light and dark theme",
    "mega_h": "Six pillars, one connected practice", "mega_p": "From the right stores to the right shelf. Each pillar answers one question a manufacturer or retailer has to get right.", "mega_all": "All six pillars",
    "impact": "Impact", "right": "Right",
    "foot_pillars": "Pillars", "foot_kiyan": "Kiyan", "foot_contact": "Get in touch", "foot_gap": "The execution gap", "foot_poc": "Free POC",
    "rights": "All rights reserved.", "sitemap": "Sitemap", "hq": "Riyadh, Saudi Arabia",
    "wa_label": "Chat with Kiyan on WhatsApp", "whatsapp": "WhatsApp", "linkedin": "LinkedIn",
    "cta_eyebrow": "Next step", "cta_h": "Ready when you are.", "cta_p": "Confirm your pilot store and category and we start this week. Or tell us the decision you are facing and we will take it from there.",
    # home
    "hero_eyebrow": "Category management & retail execution · Riyadh",
    "hero_h": "Where intelligence meets <em>execution.</em>",
    "hero_p": "Knowing is not doing. Kiyan takes strategy from the boardroom to the shelf, for the manufacturers and retailers who own it.",
    "hero_secondary": "See the six pillars", "hero_signal": "Signal", "hero_decision": "Shelf",
    "stats_label": "Kiyan in numbers",
    "stats": [("6", "", "pillars, from the right stores to the right shelf"), ("5M", "+", "retail entities scanned and mapped across three markets"),
              ("230", "+", "cities covered in Saudi Arabia"), ("18", "+", "years of retail census fieldwork behind the method")],
    "gap_eyebrow": "The execution gap", "gap_from": "Boardroom", "gap_to": "Shelf",
    "gap_impact": "What it costs when the plan does not reach the shelf",
    "q_eyebrow": "Six questions", "q_h": "Where is your gap?", "q_p": "Select every question you cannot answer with confidence. Each one is a pillar, and we will point you to where the work usually starts.",
    "q_tap": "Tap if this is a gap", "q_marked": "Marked as a gap", "q_none_h": "Nothing selected yet.", "q_none_p": "If you find a gap in any of these six questions, Kiyan is here to help you close it.",
    "q_one": "One gap: {x}.", "q_many": "{n} gaps: {x}.", "q_start": "Where the work usually starts: {x}.", "q_poc": " With several gaps open, a one-store proof of concept is the quickest way to see which matters most.",
    "q_cta": "Talk it through", "q_prefill": "From the six questions, our gaps are: {x}.",
    "p_eyebrow": "The six pillars", "p_h": "From the right stores to the right shelf.", "p_p": "Six pillars, one connected practice. The answer in one becomes the brief for the next.",
    "p_explore": "Explore {x}", "p_tabs": "Kiyan pillars",
    "how_eyebrow": "How we work", "how_h": "One table. Three roles.", "how_p": "Manufacturer and retailer bring different strengths. Kiyan, as the independent partner, structures the project and manages it end to end.",
    "how_more": "How we work",
    "proof_eyebrow": "Right execution in practice", "proof_h": "On-shelf availability is decided at the shelf. We close the loop every week.",
    "proof_p": "Field teams capture the shelf in two minutes. Image recognition reports availability, share of shelf and planogram compliance, and every gap becomes a task that is tracked until it is closed.",
    "proof_link": "See Right Execution",
    "proof_stats": [("96–98%", "audit benchmark from AI image recognition"), ("2 min", "per store audit, captured by the field force"), ("−60%", "audit cost compared with a manual audit")],
    "poc_h": "Let’s build a proof of concept.", "poc_p": "No cost, no commitment. One store, one category, one week, and you see the redesign of your shelf with the justification before deciding anything else.",
    "poc_units": ["store", "category", "week"], "poc_btn": "Confirm your pilot store",
    "people_eyebrow": "The people behind Kiyan", "people_h": "Intelligent work is still done by people.", "people_p": "Kiyan is led by partners who have run research, retail and brand businesses themselves. You work with them directly.",
    "pedigree": "Where our partners built their careers", "people_link": "Meet the team",
    "faq_eyebrow": "Questions", "faq_h": "Asked often.", "faq_p": "Short answers to what people ask before a first call.", "faq_all": "All questions",
    # pillars page
    "pp_crumb": "Pillars", "pp_eyebrow": "The six pillars", "pp_h": "Six pillars from the right stores to the right shelf.",
    "pp_p": "Each pillar answers one question a manufacturer or retailer has to get right. They can be engaged one at a time. They are built to connect, so that what is decided in the plan is what the shopper finds in the store.",
    "pp_question": "The question", "pp_solutions": "Key solutions inside this pillar", "pp_poc": "Start a free POC on this pillar",
    "roles_h": "Four category roles", "layers_h": "A store is more than its name, address and sales history.",
    "layers_p": "A retail universe is not a store list or a map of pins. It is a verified, decision-ready view of every relevant outlet: where it is, what type of store it is, what happens inside it, what surrounds it and what commercial potential it represents.",
    "layers_th": ["Layer", "What Kiyan understands", "Why it matters"],
    "layers_pull": "Most census exercises provide a directory. <em>Kiyan provides the intelligence needed to act.</em>",
    "svg_inside": "INSIDE", "svg_inside_s": "SHELF · CHILLER · DISPLAY", "svg_store": "STORE", "svg_store_s": "FORMAT · SIZE · SETUP", "svg_outside": "OUTSIDE", "svg_outside_s": "ROADS · COMPETITORS · CATCHMENT · FOOTFALL",
    "svg_label": "Three layers of store intelligence: outside the store, the store itself and inside the store",
    "rtm_h": "Find the leakage before redesigning the route.", "rtm_p": "A route can look busy while still being commercially inefficient. Kiyan examines the relationship between route activity, store coverage, product availability and cost-to-serve.",
    "rtm2_h": "Design the route around the opportunity, not the other way around.", "rtm2_p": "Kiyan does not optimise distance alone. A shorter route is not better if it misses high-potential outlets, carries the wrong assortment, creates excess frequency or delivers low-value drops.",
    "rtm_rights": ["Right stores", "Right route", "Right load", "Right frequency", "Right economics"],
    "loop": ["Design", "Deploy", "Execute", "Measure", "Refine"],
    "rtm_pull": "A better route is not the route designed on paper. <em>It is the route that performs better in the market.</em>",
    "changes": "What it changes commercially", "receive": "What you receive",
    "seg_h": "A segmentation model that tells every team what to do differently.", "seg_p": "The value of segmentation is not knowing which stores belong together. It is knowing what to do differently with each group.",
    "plano_h": "One category. Different stores. Smarter shelf decisions.", "plano_p": "A planogram must reflect the store’s segment, role and physical reality. A strong planogram is standardised in logic, but adapted to reality.",
    "plano_th": ["Store requirement", "Planogram response"],
    # how we work
    "hw_crumb": "How we work", "hw_eyebrow": "How we work", "hw_h": "One table. Three roles. One shared objective.",
    "hw_p": "Kiyan sits between manufacturer and retailer as the independent category management partner. We structure the project, integrate the data and manage it from assessment to pilot to scale.",
    "hw_brings_m": "Manufacturer brings", "hw_brings_k": "Kiyan · independent category management partner", "hw_brings_r": "Retailer brings",
    "hw_obj": "Grow the category. Create shopper value. <em>Grow together.</em>",
    "hw_chain": ["Better shopper understanding", "Better assortment, pricing, promotion and space decisions", "Stronger shopper value", "Category growth", "Retailer and manufacturer growth"],
    "pr_eyebrow": "Principles", "pr_h": "Smart about the evidence. Human about the change.", "pr_p": "Analysis decides what should happen. People decide whether it does. We plan for both.",
    "poc_eyebrow": "Proof of concept", "poc2_h": "One store, one category, one week.", "poc2_p": "No cost, no commitment. You see your shelf redesigned, with the justification, before deciding anything else.",
    "where_eyebrow": "Where we are", "where_h": "Riyadh, Istanbul, Cairo.", "where_p": "Headquartered in Riyadh, with partners in Istanbul and Cairo. We work in English and Arabic.",
    "careers_eyebrow": "Careers", "careers_h": "Work where the answer has to hold up in a store.", "careers_p": "We are a small senior team, and we are growing. If you care about what happens after the presentation, we would like to hear from you.",
    "careers_btn": "Introduce yourself", "careers_subject": "Careers at Kiyan",
    # team
    "tm_crumb": "Team", "tm_eyebrow": "The people behind Kiyan", "tm_h": "Senior people, close to the work.",
    "tm_p": "Kiyan is led by partners who have run research, retail, brand and commercial businesses across the Middle East, Türkiye and Europe. The people you meet in the first conversation are the people who do the work.",
    "tm_all": "Everyone", "tm_filter": "Filter the team by focus", "tm_career": "Career", "tm_portrait": "Portrait of {name}, {role} at Kiyan",
    "tm_join_h": "The team is growing.", "tm_join_p": "We are looking for people who are as comfortable in a store or with a field team as they are in front of a dataset. If that is you, introduce yourself.", "tm_join_btn": "Write to us",
    # faq / contact / 404
    "fq_crumb": "FAQ", "fq_h": "Frequently asked questions.", "fq_p": "Plain answers about who Kiyan is, what we do and how an engagement starts.", "fq_cant": "Cannot find what you need?", "fq_ask": "Ask us directly",
    "ct_crumb": "Contact", "ct_eyebrow": "Contact", "ct_h": "Confirm your pilot store, or tell us the decision you are facing.", "ct_p": "Start a free proof of concept, book a discovery call or send your RFP. A partner will reply.",
    "ct_type": "Enquiry type", "ct_types": ["Free POC", "Discovery call", "RFP"],
    "ct_name": "Your name", "ct_role": "Role", "ct_company": "Company", "ct_email": "Work email", "ct_topic": "Which pillar?", "ct_unsure": "Not sure yet",
    "ct_msg": "Pilot store and category, or the decision you are facing", "ct_msg_ph": "A few lines is enough. Which store and category would you pilot, or what are you trying to decide?",
    "ct_send": "Send by email", "ct_wa": "Send on WhatsApp", "ct_note": "Sending opens your own email or WhatsApp with the message filled in, so nothing is stored on this site.",
    "ct_direct": "Direct contacts", "ct_email_h": "Email", "ct_partners": "Partners", "ct_offices": "Offices", "ct_offices_p": "Headquartered in Riyadh, Saudi Arabia.",
    "m_enquiry": "Enquiry", "m_pillar": "Pillar", "m_new": "new enquiry",
    "nf_h": "This page is not on the shelf.", "nf_p": "The link may be old, or the page has moved.", "nf_btn": "Back to home",
    "s_empty": "Nothing found for “{q}”. Try a pillar, a solution or a name.",
    "k_page": "Page", "k_pillar": "Pillar", "k_solution": "Solution", "k_person": "Person", "k_question": "Question",
    # meta
    "t_home": "Kiyan | Where intelligence meets execution", "d_home": "Kiyan is a category management and retail execution consultancy in Riyadh. Six pillars take strategy from the boardroom to the shelf.",
    "t_pillars": "The six pillars: Right Reach to Right Execution | Kiyan", "d_pillars": "Kiyan's six pillars: retail census and coverage, category roles, range, store clustering, space and planograms, and AI shelf audit.",
    "t_how": "How we work: one table, three roles | Kiyan", "d_how": "Kiyan is the independent category management partner between manufacturer and retailer. How a project runs, and the free one-week proof of concept.",
    "t_team": "Our team: the partners behind Kiyan", "d_team": "Meet the partners behind Kiyan: senior leaders in research, shopper insight, retail census, category management, brand and store excellence.",
    "t_faq": "FAQ: Kiyan, the six pillars and how we work", "d_faq": "Answers about Kiyan: the six pillars, category management, retail census, AI shelf audits and the free proof of concept.",
    "t_contact": "Contact Kiyan: start a free POC or book a call", "d_contact": "Start a free one-week proof of concept, book a discovery call or submit an RFP. Email info@kiyan.sa or message Kiyan on WhatsApp.",
    "t_404": "Page not found | Kiyan",
}

GAP = {
    "title": "Strategy is rarely the problem. The shelf is where it leaks.",
    "lede": "The market is full of insight and short on action. Most companies hold the data, write the strategy and present the slides, then lose the return somewhere between the boardroom and the shelf.",
    "stages": [("Strategy written", "deck-shelves of insight", 100, "#2D6DF6", .16), ("Insight delivered", "the team reads it", 78, "#2D6DF6", .26),
               ("Action started", "handoff happens", 54, "#86BC25", .3), ("Shelf reality", "realised ROI", 34, "#86BC25", .55)],
    "points": [("Top of funnel", "Strategy is rarely the problem.", "Brand owners are well supplied with POS data, syndicated reports, supplier decks and category reviews."),
               ("Middle leak", "Insight gets lost in translation.", "Strategy and execution live in different silos. Insight rarely becomes a price tag, a planogram or a store action."),
               ("Bottom of funnel", "Reality is decided on the shelf.", "On-shelf availability, share and margin are confirmed in-store, not in the slide deck.")],
    "impacts": [("Shoppers", "Empty shelf, delayed purchases or alternatives chosen"), ("Basket", "Smaller baskets, lost sales"),
                ("Store KPIs", "Lower satisfaction and footfall"), ("Brand", "Trade spend under-delivery, brand switching")],
}

PILLARS = [
    {"id": "reach", "n": "01", "name": "Right Reach", "short": "reach",
     "q": "Are you present in the right store universe and segments, where shoppers buy?",
     "title": "Know every outlet that matters, then cover the ones that pay.",
     "lede": "A verified store universe replaces estimated counts and blind spots, so field effort is aimed at the outlets that carry the category.",
     "chips": ["Retail census", "Store universe", "Channel coverage", "Route to market"],
     "start": "retail census, store universe and coverage design",
     "cards": [("Retail census & store universe", ["Every outlet scanned and mapped to GIS coordinates: 5M+ entities across three markets.", "Stores auto-graded Gold, Silver or Bronze from the premium brands on their shelves."], "A verified store universe replaces estimated counts and blind spots."),
               ("Channel structure & coverage design", ["Outlets classified into the KSA channel framework: modern trade, self service, traditional trade, wholesale and HORECA.", "Coverage and call plans sized by outlet value, density and city tier across 230+ Saudi cities."], "Field effort aimed at the outlets that carry the category.")],
     "kpis": [("5M+", "entities scanned, three markets"), ("230+", "cities covered in KSA"), ("18+", "years of census fieldwork")]},
    {"id": "category", "n": "02", "name": "Right Category", "short": "category",
     "q": "Are you satisfied with the shopper and purchase frequency?",
     "title": "Give every category a role, then plan it jointly.",
     "lede": "Category roles are built from shopper research, trip triggers, basket and loyalty data, then carried from insight through planning to in-store execution.",
     "chips": ["Category roles", "Category captaincy", "Joint business planning", "White space"],
     "start": "category roles and joint business planning",
     "cards": [("Category captaincy architecture", ["Category roles built from shopper research, trip triggers, basket and loyalty data.", "Supplier-neutral role architecture, range and space blueprint.", "White-space identification and category innovation."], "A category growth plan led by a neutral party."),
               ("Joint business planning", ["End-to-end project management: insights, planning, in-store execution.", "Category management plan, calendar and forecasting."], "From slides to shelf.")],
     "roles": [("Destination", "A reason to choose the store.", "5–7% of categories"), ("Routine", "A frequent need. High penetration, core items.", "55–60% of categories"),
               ("Convenience", "A quick solution that reinforces the retailer as a one-stop shop.", "15–20% of categories"), ("Occasional", "A commercial opportunity with large seasonal swings.", "5–10% of categories")]},
    {"id": "range", "n": "03", "name": "Right Range", "short": "range",
     "q": "Is the 80/20 still working, or is it quietly costing you?",
     "title": "A productive assortment that protects shopper needs.",
     "lede": "It removes duplication, congestion and inventory fragmentation without losing the shopper.",
     "chips": ["Range architecture", "80/20 analysis", "Delisting simulation", "Cannibalisation"],
     "start": "range architecture and listing/delisting simulation",
     "cards": [("Range architecture", ["Range built from demand spaces: must-stock versus nice-to-have, need-state coverage, walk-out and switching risk."], "The retailer protects shopper needs; the manufacturer defends must-stock lines."),
               ("Assortment productivity & listing/delisting simulation", ["Pareto tail analysis, space-to-sales and rate of sale by store cluster.", "Simulation of what walks in or out, what switches and what is lost."], "The retailer optimises inventory; the manufacturer improves category relevance."),
               ("Cannibalisation & innovation fit testing", ["Choice-based conjoint (CBC) for true substitution and source of volume.", "Incremental versus transferable demand per SKU."], "The retailer lists incremental inventory; the manufacturer lists innovation to win.")]},
    {"id": "store", "n": "04", "name": "Right Store", "short": "store",
     "q": "Does one national planogram really fit every store cluster?",
     "title": "Cluster, map and size the opportunity store by store.",
     "lede": "Cluster-specific range, space and service models replace one national planogram.",
     "chips": ["Store clustering", "Segmentation", "Shopper flow", "Adjacency"],
     "start": "store clustering and segmentation",
     "cards": [("Store clustering & segmentation", ["Stores clustered on shopper profile, mission mix and demand-space skew.", "Cluster-specific range, space and service models instead of one national planogram."], "Higher rate of sale from cluster-fit range and store-specific planogram execution."),
               ("Category adjacency & macro space planning", ["In-store flow study mapping paths, decisions and dwell time by zone.", "Hot and cold zones identified to improve category rate of sale."], "Category penetration, basket size, visibility and experience improved.")]},
    {"id": "space", "n": "05", "name": "Right Space", "short": "space",
     "q": "Is the share of shelf in line with the share of sales and profitability?",
     "title": "Balance four needs before recommending space.",
     "lede": "The Mixed Demand Space model weighs commercial, shopper, operational and strategic needs. Planograms are built for every fixture type, from gondolas, chillers and freezers to check-out, through to a full 3D store layout.",
     "chips": ["Space to sales", "GMROS", "Macro & micro space", "Store-specific planograms"],
     "start": "space-to-sales analysis and store-specific planograms",
     "cards": [("Space-to-sales & profitability analysis", ["Share of shelf versus share of sales, margin and GMROS.", "Over-spaced and under-spaced categories identified, with the profit at stake."], "Higher return per square metre and fact-based shelf-share allocation."),
               ("Macro & micro space planning", ["Macro: category space allocation, floor plan and adjacency by store format.", "Space elasticity modelled before any change is committed."], "Better traffic flow, basket size and cross-category pull."),
               ("Store-specific planograms", ["Cluster and store-level planograms sized to real demand and fixture reality.", "Compliance and on-shelf availability tracked so executed space matches the plan."], "Shopper-centric plans implemented store by store, with better space and inventory efficiency.")]},
    {"id": "execution", "n": "06", "name": "Right Execution", "short": "execution",
     "q": "Is your on-shelf availability where it needs to be?",
     "title": "On-shelf availability is decided at the shelf. We close the loop every week.",
     "lede": "Image recognition gives a consistent, objective baseline instead of manual spot checks. Execution stays with your team; we track whether each task closed.",
     "chips": ["AI shelf audit", "OSA & share of shelf", "Compliance", "Gap to task"],
     "start": "AI shelf audit and gap-to-task closure",
     "cards": [("AI image-recognition shelf audit", ["Every store, every week: field-force capture at two minutes per audit.", "Every SKU photographed and every shelf position recorded."], "A consistent, objective baseline instead of manual spot checks."),
               ("OSA, share of shelf & planogram compliance", ["On-shelf availability, share of shelf and compliance from the same capture.", "Gaps surfaced by SKU, shelf position and store, before they cost margin."], "Share of shelf tracked against share of sales to expose execution drift."),
               ("Gap-to-task closure & verification", ["Each gap becomes a task ticket with a specific SKU, position and resolve window.", "Rebuilt shelves are re-captured the same week."], "Only closed tasks count towards the KPI.")],
     "kpis": [("96–98%", "audit benchmark"), ("2 min", "per audit"), ("−60%", "audit cost versus manual audit")]},
]

LAYERS = [("Outside the store", "Location, catchment, traffic, surrounding activity and competition", "Reveals opportunity and context"),
          ("The store itself", "Channel, format, operating profile, footprint, storage and receiving", "Defines how the store can be served"),
          ("Inside the store", "Category presence, assortment baseline, shelf reality, cooling and display", "Shows where performance can be won")]
LEAKS = [("Coverage leakage", "Viable stores in the service area that are not being reached."), ("Route leakage", "Overlapping, backtracking or unnecessarily long routes."),
         ("Assortment leakage", "Vehicle load mismatched to store needs."), ("Frequency leakage", "Stores over-visited while valuable stores are under-served."),
         ("Capacity leakage", "Vehicle or salesperson capacity used unproductively."), ("Commercial leakage", "Route effort not aligned with store potential or return.")]
RTM_CHANGES = ["Covers more relevant stores with available assets.", "Reduces unnecessary travel, overlap and backtracking.", "Matches vehicle loads to the needs of the stores served.",
               "Aligns visit frequency with potential and replenishment.", "Increases productive calls and selling time.", "Creates room for sales uplift without adding resources."]
SEGMENT_GETS = [("Store segmentation model", "Classification by performance, potential, role and investment."), ("Segment definitions & criteria", "The variables, thresholds and logic behind each segment."),
                ("Store-level segment database", "Every outlet linked to its segment and attributes."), ("Segment-specific playbooks", "Assortment, MSL, planogram, coverage and activation."),
                ("Prioritised opportunity view", "Stores where investment can unlock more potential."), ("Measurement framework", "Segment-specific KPIs for availability and sales.")]
SEGMENT_CHANGES = ["Prioritises high-potential stores rather than treating all outlets equally.", "Identifies stores where current sales understate real opportunity.",
                   "Matches assortment and MSL to each store's role and potential.", "Allocates field-force time and visit frequency more efficiently.",
                   "Improves the return from assets, promotions and activation.", "Strengthens the foundation for route-to-market, planogram and activation."]
PLANO = [("High-potential, high-volume store", "Broader assortment, more facings, stronger visibility, fuller category block"),
         ("Growth-opportunity store", "Prioritised MSL, clear hero SKUs, space to support distribution growth"),
         ("Limited-space store", "Essential assortment, compact blocking, disciplined space allocation"),
         ("Efficient-service store", "Productive core range with simple, easy-to-maintain execution standards")]

THREE = {
    "m": ["Category vision", "Shopper and consumer insights", "Brand and market expertise", "Data and analytics", "Innovation", "Investment"],
    "k": ["Category assessment", "Data integration and analytics", "Category workshops", "Assortment, pricing and space", "Execution roadmap and pilot design", "Performance measurement", "Project governance and scaling"],
    "r": ["POS and shopper data", "Commercial priorities", "Store and operational reality", "Assortment and execution", "Pilot and performance measurement", "Expansion and scale"],
}
POC_STEPS = [("Confirm the pilot", "Pick one store and one category. Send the current planogram or realogram, product images and dimensions, and the category vision, strategy and target."),
             ("We redesign the shelf", "In under a week you receive redesigned planogram scenarios, each with its justification."),
             ("Implement and evaluate", "We support the implementation and the evaluation, so the decision to scale is made on results.")]
PRINCIPLES = [("Start from the decision", "We begin with the choice a leader has to make, then work back to the evidence it needs."),
              ("Standardised in logic, adapted to reality", "One connected method across the six pillars, applied to the store, the route and the shelf as they are."),
              ("Independent by design", "Between manufacturer and retailer we hold the neutral seat and structure the work end to end."),
              ("Measured where it lands", "A plan is finished when it performs in the market. Only closed tasks count.")]

FAQ = [
    ("What is Kiyan?", "Kiyan is a category management and retail execution consultancy based in Riyadh, Saudi Arabia. It works with manufacturers and retailers as an independent partner, taking strategy from the boardroom to the shelf through six pillars: Right Reach, Right Category, Right Range, Right Store, Right Space and Right Execution."),
    ("What does “where intelligence meets execution” mean?", "It means the work does not stop at the insight or the strategy. Most companies already hold the data and the plan; the return is lost between the decision and the shelf. Kiyan works across that gap, from census and analysis through to the planogram, the route and the store."),
    ("What are Kiyan’s six pillars?", "Right Reach (retail census, store universe and coverage); Right Category (category roles and joint business planning); Right Range (range architecture and assortment productivity); Right Store (store clustering, segmentation and adjacency); Right Space (space-to-sales analysis and store-specific planograms); and Right Execution (AI shelf audit, on-shelf availability and gap-to-task closure)."),
    ("Who does Kiyan work with?", "Manufacturers and retailers who own the shelf, and the leaders responsible for it: commercial, sales, category, trade marketing and insight teams. Kiyan is headquartered in Riyadh and works across Saudi Arabia and the wider region."),
    ("What is the execution gap?", "The execution gap is the value lost between a strategy being written and the result appearing on the shelf. Strategy and execution usually sit in different teams, so insight rarely becomes a price tag, a planogram or a store action. On-shelf availability, share and margin are confirmed in-store, which is why Kiyan measures its work there."),
    ("What is category management, and how does Kiyan approach it?", "Category management is the practice of running a product category as a business unit, so that range, pricing, promotion and shelf space are planned around how shoppers buy. Kiyan acts as an independent category management partner between manufacturer and retailer: it runs the category assessment, integrates the data, facilitates the workshops and manages the project from plan to pilot to scale."),
    ("What is a retail census or store universe?", "A retail census is a physical count and classification of every relevant outlet in a market. Kiyan’s store universe goes further than a directory: each outlet is mapped to GIS coordinates and understood on three layers, which are what surrounds it, the store itself and what happens inside it. The underlying fieldwork spans 5M+ entities across three markets and 230+ cities in Saudi Arabia."),
    ("How does the AI shelf audit work?", "Field teams photograph the shelf, which takes about two minutes per audit. Image recognition then reports on-shelf availability, share of shelf and planogram compliance from the same capture, against a 96–98% audit benchmark and at around 60% lower cost than a manual audit. Each gap becomes a task with a specific SKU, position and resolve window, and the shelf is re-captured to verify closure."),
    ("What is the free proof of concept?", "Kiyan offers a proof of concept at no cost and with no commitment: one store, one category, one week. You share the current planogram or realogram for the pilot store, product images and dimensions, and your category vision. Kiyan returns redesigned planogram scenarios with the justification, and supports implementation and evaluation."),
    ("What is route-to-market optimisation?", "Route-to-market (RTM) optimisation designs sales and delivery routes around store potential rather than distance alone. Kiyan first diagnoses six kinds of leakage (coverage, route, assortment, frequency, capacity and commercial), then rebuilds the model so the right stores get the right route, load, frequency and economics."),
    ("Where is Kiyan based?", "Kiyan is headquartered in Riyadh, Saudi Arabia, with a presence in Istanbul and Cairo."),
    ("How do I start working with Kiyan?", "Confirm a pilot store and category for a free proof of concept, book a discovery call, or send your RFP to info@kiyan.sa."),
]
HOME_FAQ = [0, 2, 3, 8, 11]
FIRMS = ["Nielsen", "GfK", "MAF Carrefour", "Apple", "Nike", "KPMG", "BAT", "Curiosity"]
FOCUS_LABELS = {}

UI.update({
    "role_tag_m": "Manufacturer", "role_tag_k": "Kiyan · independent partner", "role_tag_r": "Retailer",
    "role_h_m": "Brings the category vision.", "role_h_k": "Structures the work, end to end.", "role_h_r": "Brings the store reality.",
    "car_prev": "Previous partner", "car_next": "Next partner", "car_label": "Kiyan partners", "prev_at": "Career",
    "mega_feat_tag": "Free proof of concept", "mega_feat_h": "One store, one category, one week.", "mega_feat_p": "See your shelf redesigned, with the justification, before deciding anything else.",
    "mega_more_h": "Kiyan",
    "lg_terms": "Terms of Use", "lg_privacy": "Privacy Policy", "lg_security": "Security", "lg_cookies": "Cookie Preferences",
    "lg_crumb": "Legal", "lg_h": "Terms, privacy, security and cookies.", "lg_p": "How this website may be used and what it does with your information. Last updated November 2026.",
    "t_legal": "Terms, privacy, security and cookies | Kiyan", "d_legal": "Kiyan's website terms of use, privacy policy, security statement and cookie preferences.",
    "lang_current": "English",
})
LEGAL = [
    ("terms", "Terms of Use", [
        "This website is published by Kiyan, Riyadh, Saudi Arabia, to describe its services. By using it you accept these terms.",
        "The content is general information, not professional advice. An engagement with Kiyan is governed only by the signed agreement for that engagement.",
        "The Kiyan name, logo, text, illustrations and photographs on this site belong to Kiyan or its licensors. You may share links and quote short passages with attribution; other reuse needs written permission.",
        "We work to keep the site accurate and available, but it is provided as it is, without warranty. Links to other websites are provided for convenience and we are not responsible for their content.",
    ]),
    ("privacy", "Privacy Policy", [
        "This website does not ask you to create an account and does not run advertising or third-party tracking scripts.",
        "The contact form does not store your details on this website. It opens your own email or WhatsApp application with the message filled in, and nothing is sent until you choose to send it.",
        "When you email or message us, we receive what you send (such as your name, company, email address and message) and use it only to reply and to discuss working together. We do not sell personal information.",
        "You can ask us to correct or delete the information you have sent by writing to info@kiyan.sa. We handle personal data in line with the Saudi Personal Data Protection Law.",
    ]),
    ("security", "Security", [
        "This website is a static site served over HTTPS. It has no login, no database and no payment processing, which keeps its exposure small.",
        "Fonts, scripts and images are served from this site itself, so pages do not load code from third parties.",
        "Client data shared during an engagement is handled under the confidentiality and data terms of that engagement, not through this website.",
        "To report a security concern, write to info@kiyan.sa.",
    ]),
    ("cookies", "Cookie Preferences", [
        "This website does not set advertising or analytics cookies, so there is nothing to opt in to or out of.",
        "Your browser stores one preference on your own device: whether you chose the light or dark theme. It is not sent to us and you can clear it at any time from your browser settings.",
        "If analytics are added in future, this section will be updated and you will be asked for consent first where the law requires it.",
    ]),
]

UI.update({
    "nav_company": "Company",
    "mg_p_h": "The six pillars", "mg_p_d": "From the right stores to the right shelf. One connected practice for manufacturers and retailers.",
    "mg_c_h": "Kiyan", "mg_c_d": "An independent category management and retail execution partner, headquartered in Riyadh.",
    "mg_items": [("how-we-work.html", "table", "How we work", "One table, three roles, one shared objective"),
                 ("index.html#execution-gap", "gap", "The execution gap", "Why value leaks between plan and shelf"),
                 ("team.html", "people", "Team", "The partners who do the work"),
                 ("how-we-work.html#poc", "flask", "Free proof of concept", "One store, one category, one week"),
                 ("faq.html", "help", "FAQ", "Plain answers before a first call"),
                 ("how-we-work.html#careers", "case", "Careers", "Join a small senior team"),
                 ("contact.html", "mail", "Contact", "Riyadh, Istanbul and Cairo")],
    "mg_promo_link": "Confirm your pilot store",
})
for _p, _d in zip(PILLARS, ["Retail census, store universe and coverage", "Category roles and joint business planning", "Range architecture and assortment productivity",
                            "Store clustering, segmentation and adjacency", "Space-to-sales analysis and planograms", "AI shelf audit and gap-to-task closure"]):
    _p["menu"] = _d

UI.update({
    "pl_top": "Category management & retail execution", "pl_words": ["Where", "intelligence", "meets", "<em>execution.</em>"], "pl_bars": "Six pillars",
    "pg_names": {"index.html": "Home", "pillars.html": "Pillars", "how-we-work.html": "How we work", "team.html": "Team", "faq.html": "FAQ", "contact.html": "Contact", "legal.html": "Legal", "404.html": "Kiyan"},
})
