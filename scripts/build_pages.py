"""Generate static project and notebook pages. No third-party dependencies."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent

PROJECTS = [
    {
        'id': 'ucl', 'section': 'experience', 'label': 'Research experience / UCLR risk prediction',
        'title': 'Predicting UCL reconstruction risk in MLB pitchers',
        'description': 'Comparing nine machine learning approaches to a sports-medicine question, with interpretation alongside prediction.',
        'meta': ['Georgia Institute of Technology School of Mathematics', 'May 2024–June 2025', 'IEEE ICHI 2025', 'Oral presentation', 'Lead & corresponding author'],
        'body': '''
<h2>The question</h2>
<p>Can machine learning help identify patterns associated with ulnar collateral ligament reconstruction in professional baseball pitchers? This study compares conventional classifiers, ensembles, and neural decision-tree approaches on MLB data spanning approximately 2016–2024.</p>
<h2>Study design</h2>
<p>Cases were matched on relevant factors including age and debut year. Nine models were compared: logistic regression, K-nearest neighbors, support vector machines, decision trees, random forests, XGBoost, artificial neural networks, deep neural decision trees, and deep neural decision forests.</p>
<p>The goal was to compare predictive approaches within the study design and examine the features informing their predictions. SHAP was used for interpretability.</p>
<h2>Reported results</h2>
<table><caption>Approximate accuracy reported in the study</caption><thead><tr><th scope="col">Model</th><th scope="col">Accuracy</th></tr></thead><tbody><tr><td>Deep Neural Decision Forest</td><td>~79.2%</td></tr><tr><td>Random Forest</td><td>~71.9%</td></tr></tbody></table>
<div class="callout"><p>These values describe performance within this study. They should not be read as evidence of clinical readiness, individual treatment utility, or generalization to a different population.</p></div>
<h2>Contribution and presentation</h2>
<p>I was lead and corresponding author and presented the work orally at IEEE ICHI 2025. Conference travel was funded by approximately <strong>$3,500 in National Science Foundation grant support</strong>.</p>
<h2>Publication title</h2>
<p><em>Comparative Machine Learning Analysis Highlights Novel Predictive Capability of Deep Neural Decision Forest for Ulnar Collateral Ligament Reconstruction in Baseball Athletes.</em></p>
<h2>How this connects to my direction</h2>
<p>This work is part of my foundation in biomedical prediction: relating model comparisons to a domain question, interpreting learned associations, and keeping the distinction between a useful prediction and an actionable intervention visible.</p>'''
    },
    {
        'id': 'entropy', 'section': 'projects', 'label': 'Projects / Sparse Semantic Entropy Probes',
        'title': 'Sparse Semantic Entropy Probes',
        'description': 'Investigating whether sparse internal representations can help detect unreliable language-model outputs.',
        'meta': ['August 2026–present', 'Preliminary results'],
        'body': '''
<h2>The question</h2>
<p>Which internal representations are predictive of language-model correctness, and can a small subset of sparse features provide a useful reliability signal? This project brings together sparse autoencoders, feature attribution, semantic entropy, and statistical feature selection.</p>
<h2>Stage I: locate informative layers</h2>
<p>The first stage explores where reliability-related information becomes accessible across a model’s layers. The aim is to identify sharp changes in predictiveness and select layers for closer analysis. A working experimental setting used <strong>Gemma-Scope-16k features at layer 20</strong>.</p>
<h2>Stage II: examine individual features</h2>
<p>The next stage studies feature-level attribution and compares methods for selecting useful features. A conceptual attribution score combines feature activation with the alignment of its decoder direction to an output-token direction:</p>
<div class="callout"><p><code>A_i(t) = s_i (w_dec^(i))ᵀ W_U[:, t]</code></p><p>Here, <code>s_i</code> is the feature activation, <code>w_dec^(i)</code> its decoder direction, and <code>W_U[:, t]</code> the unembedding direction for token <code>t</code>.</p></div>
<h2>Experimental snapshot</h2>
<p>Experiments involved approximately <strong>7,382 prompts</strong>. Mean-difference selection with approximately 128 features produced a best observed AUROC of roughly <strong>0.818</strong>.</p>
<table><caption>Representative preliminary AUROC values</caption><thead><tr><th scope="col">Feature-selection method</th><th scope="col">AUROC</th></tr></thead><tbody><tr><td>Mean difference</td><td>~0.818</td></tr><tr><td>Pearson correlation</td><td>~0.816</td></tr><tr><td>Mann–Whitney U</td><td>~0.816</td></tr><tr><td>Spearman correlation</td><td>~0.815</td></tr><tr><td>Elastic Net</td><td>~0.798</td></tr><tr><td>Mutual information</td><td>~0.774</td></tr></tbody></table>
<p>These are working experimental results. Small differences should not be interpreted as established advantages without uncertainty estimates, held-out validation, and a full account of feature selection and evaluation.</p>
<h2>What I want to understand next</h2>
<ul><li>Whether selected features transfer across datasets and kinds of questions.</li><li>Whether predictiveness survives controls for response length, token identity, and other shortcuts.</li><li>Whether a feature is causally relevant to a model’s behavior, beyond being correlated with correctness.</li></ul>'''
    },
    {
        'id': 'ablations', 'section': 'projects', 'label': 'Projects / Partial-input reasoning ablations',
        'title': 'No Question, No Passage, No Problem: Investigating Artifact Exploitation and Reasoning in Multiple-Choice Reading Comprehension',
        'description': 'Partial-input ablations for multiple-choice reasoning: investigating what benchmarks actually measure.',
        'meta': ['May 2025–present', 'RANLP 2025 Student Research Workshop', 'NeurIPS 2025 workshops'],
        'body': '''
<h2>The question</h2>
<blockquote>How much can a language model infer when it sees only part of a multiple-choice problem?</blockquote>
<p>A benchmark score can reflect more than the reasoning capability the benchmark is intended to measure. This project investigates the contribution of individual input components and the information available in incomplete prompts.</p>
<h2>Ablating the input</h2>
<p>The experiments examine passage-only, question-only, choices-only, combined partial inputs, and full-input conditions. Datasets include <strong>QuALITY Easy, QuALITY Hard, RACE High, ReClor, and LogiQA2</strong>, alongside out-of-distribution datasets.</p>
<p>The comparison asks whether a model can exploit answer priors, dataset artifacts, or other shortcuts when the information needed for the intended reasoning task is absent.</p>
<h2>Controls that matter</h2>
<ul><li><strong>Paraphrasing:</strong> examine sensitivity to wording and surface cues.</li><li><strong>Answer randomization:</strong> probe dependence on choice ordering.</li><li><strong>Prior flattening:</strong> examine the contribution of answer priors.</li><li><strong>Out-of-distribution evaluation:</strong> assess how conclusions change across datasets.</li></ul>
<h2>Research context</h2>
<p>The work was accepted or presented in contexts including the <strong>RANLP 2025 Student Research Workshop</strong> and NeurIPS 2025 workshops related to language-model evaluation and efficient reasoning.</p>
<h2>Why this work matters to my direction</h2>
<p>The central habit is to ask what an evaluation supports. As I move into biological ML, I want to bring the same attention to split design, hidden shortcuts, and whether a task measures the capability a scientific user needs.</p>'''
    },
    {
        'id': 'nfl', 'section': 'experience', 'label': 'Research experience / NFL injured reserve prediction',
        'title': 'NFL injured reserve prediction',
        'description': 'Predictive modeling with temporal evaluation and feature attribution for wide receivers and tight ends.',
        'meta': ['The Wharton School Institute of AI and Analytics', 'June 2025–October 2025', 'Lead & corresponding author', 'IEEE MIT URTC 2025'],
        'body': '''
<h2>The question</h2>
<p>Can performance, exposure, and prior-injury information help predict injured-reserve outcomes for NFL wide receivers and tight ends?</p>
<h2>Temporal evaluation</h2>
<p>The dataset includes approximately <strong>746 player-seasons</strong> and <strong>152 positive injured-reserve cases</strong>. Training data covers 2018–2022, with 2023 used for testing. This separates model fitting from a later season rather than mixing seasons across the evaluation.</p>
<h2>Features and models</h2>
<p>Representative features include targets, yards, average cushion, total snaps, forty-yard dash time, and previous injured-reserve count. The study compares XGBoost, a multilayer perceptron, and a random forest.</p>
<table><caption>Approximate balanced accuracy on the temporal test</caption><thead><tr><th scope="col">Model</th><th scope="col">Balanced accuracy</th></tr></thead><tbody><tr><td>XGBoost</td><td>~58.3%</td></tr><tr><td>MLP</td><td>~57.0%</td></tr><tr><td>Random Forest</td><td>~55.9%</td></tr></tbody></table>
<h2>Interpretation</h2>
<p>SHAP drivers included forty-yard dash time, average cushion, and total snaps. These are model associations, not evidence that changing a feature would change an athlete’s injury risk.</p>
<p>The modest balanced accuracies make the limitations visible. The study offers experience with temporal evaluation, explainability, and predictive modeling in a health-related domain; it does not establish a deployable clinical decision tool.</p>'''
    },
    {
        'id': 'biofm', 'draft': True, 'section': 'projects', 'label': 'Projects / Emerging AI-for-science project',
        'title': 'Molecular visualization / BioFM playground',
        'description': 'A planned research environment for connecting protein sequence, structure, and learned representations.',
        'meta': ['Design stage', 'Exploratory builder project', 'Capabilities below are planned'],
        'body': '''
<h2>The idea</h2>
<p>I want a workspace where a protein’s sequence, structure, and learned features can be explored together. Selecting a residue would connect its sequence position with its structural neighborhood and model representation.</p>
<div class="callout"><p><strong>Current stage: project design.</strong> The roadmap below describes intended capabilities, rather than a completed molecular viewer or model integration.</p></div>
<h2>A staged roadmap</h2>
<ol><li><strong>Structure first.</strong> Load PDB structures and support rotation, zoom, residue selection, chain coloring, and secondary-structure coloring.</li><li><strong>Representation overlays.</strong> Explore protein-language-model embeddings from accessible models such as ESM or ProtT5, with explicit provenance for each model and input.</li><li><strong>Embedding views.</strong> Add PCA, UMAP, or t-SNE where appropriate, while making projection choices visible.</li><li><strong>Linked sequence and structure.</strong> Selecting a residue highlights its sequence position, representation, and structural neighborhood.</li><li><strong>Compare models.</strong> Investigate which patterns are consistent across representations, and which depend on the model or layer.</li></ol>
<h2>Design principles</h2>
<p>Keep the environment useful for asking a concrete research question. Distinguish observed structure from predictions, model confidence from experimental certainty, and a visually interesting projection from evidence about biological function.</p>
<h2>What this project is for</h2>
<p>This is a deliberate step into biological ML: learning how model inputs, representations, structural context, and evaluation fit together while building a tool that makes those relationships inspectable.</p>'''
    }
]

BUILDS = [
    {
        'id': 'isotope', 'label': 'Projects / Isotope',
        'title': 'Isotope',
        'description': 'Making dependency and API upgrades safer with behavioral comparisons and independently verified repairs.',
        'meta': ['HopHacks 2026', 'Winner: Strategy Sponsor Track', 'Team project · Working GitHub Action'],
        'body': '''
<div class="callout"><p><strong>Our team won the Strategy Sponsor Track at HopHacks 2026.</strong> I helped build Isotope into a working GitHub Action, bringing code analysis, isolated execution, and LLM-assisted reasoning into a local-first CI workflow.</p></div>
<p><a href="https://github.com/hmartel222/Isotope">View Isotope on GitHub ↗</a></p>
<h2>The problem</h2>
<p>Dependency and API upgrades can change what an application does even when its code still compiles. Isotope investigates the effect of an upgrade on the application’s behavior and checks whether a proposed repair actually preserves the intended result.</p>
<h2>How it works</h2>
<ol><li><strong>Identify affected code.</strong> Use static analysis to locate the parts of an application that depend on a changed API or dependency.</li><li><strong>Compare old and new behavior.</strong> Run isolated executions to make the consequences of an upgrade observable.</li><li><strong>Reason about the difference.</strong> Combine execution evidence with LLM-assisted reasoning when a change requires further interpretation.</li><li><strong>Verify proposed repairs independently.</strong> Check a candidate fix through separate execution rather than accepting the repair proposal itself as evidence.</li></ol>
<h2>My contribution</h2>
<p>I helped build the project with my team as a local-first CI workflow using <strong>TypeScript/Node, static analysis, isolated execution, and LLM-assisted reasoning</strong>. The result was a working GitHub Action that brings upgrade analysis and repair verification into the development workflow.</p>
<h2>Why this matters to my work</h2>
<p>Isotope connects my interests in reliable AI and research engineering: make the behavior observable, preserve the evidence, and evaluate a proposed intervention independently.</p>'''
    },
    {
        'id': 'alpharx', 'label': 'Projects / Data & research systems',
        'title': 'AlphaRx',
        'description': 'A working research prototype exploring population-health signals and healthcare-sector market behavior.',
        'meta': ['Side project', 'Working research prototype', 'No public repository yet'],
        'body': '''
<h2>The question</h2>
<p>Do population-health signals, such as CDC influenza surveillance and Google Trends, contain incremental information for forecasting healthcare-sector market behavior?</p>
<h2>What I built</h2>
<p>I built the data and modeling pipeline around <strong>point-in-time data integration, feature engineering, and out-of-sample evaluation</strong>. The infrastructure uses Python, Docker, PostgreSQL, and Airflow to support reproducible data processing and experimentation.</p>
<h2>Research priorities</h2>
<ul><li>Track when information would have been available to a model.</li><li>Compare signals against appropriate baselines on observations outside the training data.</li><li>Keep ingestion, feature construction, and evaluation reproducible.</li></ul>
<h2>Current stage</h2>
<p>AlphaRx exists as a <strong>working research prototype</strong>. It is an investigation into data and forecasting methodology, with no claim of a finished trading system or established financial performance. There is no public project link yet.</p>'''
    },
    {
        'id': 'glucagone', 'label': 'Projects / Healthcare',
        'title': 'GlucaGone',
        'description': 'A diabetes-related app exploring machine learning and understandable health information.',
        'meta': ['2025 project', 'Healthcare ML', 'Web application'],
        'body': '''
<h2>Overview</h2>
<p>GlucaGone is a diabetes-related application exploring how machine learning can support more understandable health information.</p>
<p>The project is part of my broader interest in building practical tools around health-related data and making model outputs easier to interpret.</p>'''
    }
]

NOTES = [
    {
        'id': 'protein-language-models', 'label': 'Research notebook / Note 001',
        'title': 'What does a protein language model actually learn?',
        'description': 'A starting point for thinking about sequence representations and the experiments needed to understand them.',
        'meta': ['Concept sketch', 'September 2026', 'Biological foundation models'],
        'body': '''
<h2>A useful starting point</h2>
<p>A protein language model can learn from the statistical patterns in amino-acid sequences. In masked-sequence training, it learns to predict hidden residues from the surrounding context. Rives and colleagues showed that large-scale sequence learning can produce representations containing information about biological structure and function. <a href="https://doi.org/10.1073/pnas.2016239118">Rives et al., PNAS (2021)</a>.</p>
<h2>Three questions I want to keep separate</h2>
<ol><li><strong>What information is present?</strong> Can a probe recover a structural or functional property from the representation?</li><li><strong>What information is used?</strong> Does changing a representation change the model’s behavior in a way consistent with the proposed interpretation?</li><li><strong>What information is useful?</strong> Does it improve a decision on proteins that differ meaningfully from the training examples?</li></ol>
<p>These are the questions I want to use to organize my reading. A representation that supports a good probe is a promising starting point; I would still want to investigate what the probe can exploit.</p>
<h2>An experiment I would like to run</h2>
<p>Compare representations across layers on one clearly defined biological property. Start with a simple probe, control its capacity, and compare against sequence-level baselines. Then repeat the evaluation using splits that make sequence similarity visible.</p>
<p>The result I would find most useful is an account of which signals transfer, where they fail, and which next experiment could distinguish a biological explanation from a shortcut.</p>'''
    },
    {
        'id': 'prediction-intervention', 'label': 'Research notebook / Note 002',
        'title': 'From prediction to intervention in biological ML',
        'description': 'What has to happen between a strong model result and a useful scientific decision?',
        'meta': ['Concept sketch', 'September 2026', 'AI for therapeutics'],
        'body': '''
<h2>A prediction is a starting point</h2>
<p>AlphaFold 3 illustrates the expanding scope of biomolecular prediction, modeling structures of complexes involving proteins and other molecular components. That makes it a useful reference point for a question I care about: how should a predicted interaction inform the next experiment? <a href="https://www.nature.com/articles/s41586-024-07487-w">Abramson et al., Nature (2024)</a>.</p>
<h2>Work backward from the decision</h2>
<p>When I think about a biological ML project, I want to start with a specific user and decision. Is a scientist choosing a target, ranking candidates for an assay, or deciding which hypothesis to test? Each decision suggests a different evaluation.</p>
<p>A useful project description should say what the model observes, what it predicts, and what action that prediction could support. It should also say which uncertainties remain unresolved.</p>
<h2>Questions for an evaluation</h2>
<ul><li>What experimental budget or constraint is the model meant to help with?</li><li>Does the test set reflect the kind of new candidate the scientist would encounter?</li><li>Which errors are expensive, and can the model express uncertainty about them?</li><li>What experiment could disprove the proposed interpretation?</li></ul>
<h2>My working direction</h2>
<p>I want to connect representation learning with decisions that can be investigated experimentally. In my own trajectory, that means building a stronger understanding of biology alongside modeling and evaluation. Therapeutic discovery is the direction I am working toward, and these are the questions I want to bring to it.</p>'''
    },
    {
        'id': 'interpretability-biology', 'label': 'Research notebook / Note 003',
        'title': 'Mechanistic interpretability outside language models',
        'description': 'An open research question: which tools for understanding language-model features could help us inspect biological representations?',
        'meta': ['Research question', 'September 2026', 'Interpretability'],
        'body': '''
<h2>The connection I want to explore</h2>
<p>Gemma Scope provides sparse autoencoders for studying internal representations in Gemma 2. These tools decompose activations into sparse features that researchers can inspect. My work with SAE features motivates a question about whether related approaches could be useful for biological foundation models. <a href="https://arxiv.org/abs/2408.05147">Lieberum et al., Gemma Scope (2024)</a>.</p>
<p>I am treating that transfer as a research question. An interpretable feature in a protein model would need a biological account of what it represents and evidence that the account survives appropriate controls.</p>
<h2>A possible investigation</h2>
<ol><li>Choose a representation and a narrowly defined biological property.</li><li>Inspect whether sparse features associate with that property across diverse sequences.</li><li>Compare against simpler probes and sequence-derived baselines.</li><li>Check sensitivity to model layer, feature selection, and sequence similarity.</li><li>Where feasible, investigate whether interventions on a feature have a consistent effect on the model’s output.</li></ol>
<h2>What would convince me?</h2>
<p>I would want evidence beyond a compelling visualization or a small set of examples. My working standard is a feature whose proposed interpretation predicts behavior on held-out cases, survives confounder checks, and suggests a useful next experiment.</p>
<p>This is one place where my existing interest in interpretability meets my emerging focus on biological ML. The connection is worth investigating precisely because its usefulness should be tested.</p>'''
    }
]

def render(page, kind, next_page):
    section = page.get('section', kind)
    group_label = {'experience': 'Research experience', 'work': 'Research experience', 'projects': 'Projects', 'notes': 'Research notebook'}[section]
    back_label = {'experience': 'research experience', 'work': 'research experience', 'projects': 'projects', 'notes': 'the notebook'}[section]
    next_url = f'../../{kind}/{next_page["id"]}/'
    if page['id'] == 'biofm':
        next_url = '../../projects/isotope/'
    if page['id'] == 'ucl':
        next_url = '../../work/nfl/'
    elif page['id'] == 'nfl':
        next_url = '../../work/ucl/'
    elif page['id'] == 'ablations':
        next_url = '../../projects/isotope/'
    robots = '<meta name="robots" content="noindex">' if kind == 'notes' else ''
    back_url = '../../' if kind == 'notes' else f'../../#{section}'
    if kind == 'notes':
        group_label = 'Home'
        back_label = 'home'
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{robots}<meta name="theme-color" content="#ffffff"><meta name="description" content="{escape(page['description'], quote=True)}">
<meta property="og:title" content="{escape(page['title'], quote=True)} · Rohan Butani"><meta property="og:description" content="{escape(page['description'], quote=True)}"><meta property="og:type" content="article">
<title>{escape(page['title'])} · Rohan Butani</title><link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600&family=Newsreader:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../styles.css"><script src="../../app.js" defer></script></head><body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header detail-header"><a class="identity" href="../../" aria-label="Rohan Butani home"><span class="monogram">rb<span>.</span></span><span class="identity-text">Rohan Butani<small>research / engineering</small></span></a><a class="detail-nav" href="{back_url}">← {group_label}</a><a class="cv-link" href="../../cv.html">CV ↗</a></header>
<main id="main" class="section-wrap detail-main"><a class="back-link" href="{back_url}">← Back to {back_label}</a><p class="eyebrow section-label">{escape(page['label'])}</p><h1>{escape(page['title'])}</h1><p class="detail-subtitle">{escape(page['description'])}</p><div class="detail-meta">{''.join('<span>' + escape(item) + '</span>' for item in page['meta'])}</div><article class="detail-body" aria-label="{'Notebook entry' if kind == 'notes' else 'Project details'}">{page['body']}</article><div class="detail-end"><a href="mailto:rbutani1@jh.edu">Discuss this {'question' if kind == 'notes' else 'work'} ↗</a><a href="{next_url}">Next {'note' if kind == 'notes' else 'project'} →</a></div></main>
<footer class="site-footer section-wrap"><span>© <span id="year">2026</span> Rohan Butani</span><a href="../../">Back to home ↗</a></footer></body></html>'''

for kind, pages in [('work', PROJECTS), ('notes', NOTES), ('projects', BUILDS)]:
    pages = [page for page in pages if not page.get('draft', False)]
    for i, page in enumerate(pages):
        directory = ROOT / kind / page['id']
        directory.mkdir(parents=True, exist_ok=True)
        (directory / 'index.html').write_text(render(page, kind, pages[(i + 1) % len(pages)]))
print(f'Generated {sum(not p.get("draft", False) for p in PROJECTS + BUILDS)} research/project pages and {len(NOTES)} notebook pages.')
