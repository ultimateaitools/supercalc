# -*- coding: utf-8 -*-
"""
add_details.py - Adds SEO-rich info sections, FAQs, and related calculators
to all thin calculator pages (those without info-box class).
"""
import os, re

BASE = r"d:\Datomate AI Lab\CalcWebsite"

def info_box(title, paras, how_steps=None, tips=None, formula=None, table_html=None):
    html = f'<div class="info-box">\n<h2>What is a {title}?</h2>\n'
    for p in paras:
        html += f'<p>{p}</p>\n'
    if formula:
        html += f'<h3>Formula</h3>\n<div class="formula-box">{formula}</div>\n'
    if how_steps:
        html += f'<h3>How to Use This Calculator</h3>\n<ol>\n'
        for s in how_steps: html += f'<li>{s}</li>\n'
        html += '</ol>\n'
    if tips:
        html += f'<h3>Key Facts &amp; Tips</h3>\n<ul>\n'
        for t in tips: html += f'<li>{t}</li>\n'
        html += '</ul>\n'
    if table_html:
        html += table_html
    html += '</div>\n'
    return html

def faq_box(faqs):
    html = '<div class="info-box">\n<h2>Frequently Asked Questions</h2>\n'
    for q, a in faqs:
        html += f'''<div class="faq-item">
<button class="faq-question">{q} <i class="bi bi-chevron-down faq-icon"></i></button>
<div class="faq-answer"><div class="faq-answer-inner">{a}</div></div>
</div>\n'''
    html += '</div>\n'
    return html

def related_box(items):
    html = '<div class="info-box">\n<h3 style="margin-top:0">Related Calculators</h3>\n<div class="related-grid">\n'
    for name, url, icon in items:
        html += f'<a href="{url}" class="related-item text-decoration-none">{icon} {name}</a>\n'
    html += '</div>\n</div>\n'
    return html

# ─── CONTENT LIBRARY ────────────────────────────────────────────────────────

CONTENT = {}

# ── INSTAGRAM ──
CONTENT["instagram-engagement-rate-calculator.html"] = (
    info_box("Instagram Engagement Rate Calculator",
        ["Instagram Engagement Rate (ER) measures how actively your audience interacts with your content relative to your total followers. It is one of the most important metrics for brands and influencers to evaluate the effectiveness of their content strategy.",
         "A high engagement rate signals that your content resonates with your audience, which makes you more attractive to brand partnerships and increases your organic reach on the Instagram algorithm."],
        ["Enter your total Instagram follower count", "Enter average likes and comments per post", "Select number of posts being averaged", "Click Calculate to get your engagement rate and quality rating"],
        ["Micro-influencers (1K-100K) typically have higher ER (3-8%) than mega influencers (1-2%)",
         "Instagram's algorithm rewards high engagement by showing your content to more users",
         "Saves and shares are weighted more heavily than likes in the algorithm",
         "A consistent posting schedule helps maintain and grow your engagement rate",
         "Respond to comments within the first hour to boost algorithmic reach"],
        table_html='''<h3>Instagram Engagement Rate Benchmarks 2025</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.83rem">
<thead><tr><th>ER Range</th><th>Rating</th><th>Account Type</th></tr></thead>
<tbody>
<tr><td>&lt;1%</td><td style="color:#ef4444">Poor</td><td>Mega influencer or inactive audience</td></tr>
<tr><td>1-3%</td><td style="color:#f59e0b">Average</td><td>Large accounts (100K+ followers)</td></tr>
<tr><td>3-6%</td><td style="color:#10b981">Good</td><td>Mid-tier influencers (10K-100K)</td></tr>
<tr><td>6-10%</td><td style="color:#6366f1">Excellent</td><td>Micro-influencers (1K-10K)</td></tr>
<tr><td>&gt;10%</td><td style="color:#8b5cf6">Outstanding</td><td>Nano influencers or viral content</td></tr>
</tbody></table></div>'''),
    faq_box([
        ("What is a good Instagram engagement rate in 2025?",
         "A good Instagram engagement rate depends on your account size. For nano-influencers (under 1K), 5-10%+ is excellent. Micro-influencers (1K-100K) should aim for 3-6%. Mid-tier accounts (100K-500K) average 1-3%. Mega influencers (1M+) often see 1-2% or below, which is still considered normal."),
        ("Why is my Instagram engagement rate dropping?",
         "Common reasons include: posting inconsistently, a shift in Instagram's algorithm, content not resonating with your current audience, increase in followers without a corresponding increase in engagement (sometimes from inactive accounts), or changes in the type of content you're posting."),
        ("Does Instagram count Story views in engagement rate?",
         "Standard engagement rate calculations use feed post data (likes + comments ÷ followers). Story views are separate metrics. However, if you're calculating engagement for Reels, views, likes, comments, and shares are all factored in."),
        ("How do I improve my Instagram engagement rate?",
         "Post at optimal times when your audience is most active, use relevant hashtags (5-15 targeted ones), ask questions in captions, respond to every comment quickly, use polls and interactive stickers in Stories, and create content that encourages saves and shares.")
    ]),
    related_box([
        ("Instagram Growth Rate","instagram-growth-rate-calculator.html","&#128200;"),
        ("Instagram Influencer Earnings","instagram-influencer-earnings-calculator.html","&#128176;"),
        ("TikTok Engagement Rate","tiktok-engagement-rate-calculator.html","&#127925;"),
        ("YouTube Engagement Rate","youtube-engagement-rate-calculator.html","&#127909;"),
        ("Social Media ROI","social-media-roi-calculator.html","&#128200;"),
        ("Virality Score Calculator","virality-score-calculator.html","&#128293;"),
    ])
)

CONTENT["youtube-money-calculator.html"] = (
    info_box("YouTube Money Calculator",
        ["YouTube pays content creators through its YouTube Partner Program (YPP). Revenue is generated from ads shown on your videos, and the amount you earn depends on CPM (Cost Per Mille - what advertisers pay per 1,000 ad impressions) and your RPM (Revenue Per Mille - what you actually receive after YouTube's 45% cut).",
         "YouTube earnings vary dramatically based on content niche, audience geography, video length, ad formats, and seasonality. Finance and business channels earn 3-5x more than gaming or entertainment channels."],
        ["Enter your average daily or monthly views", "Select your content niche (affects CPM rate)", "Enter monetized view percentage (typically 40-60%)", "Click Calculate to see daily, monthly, and yearly earnings"],
        ["YouTube keeps 45% of ad revenue; you receive 55%", "Finance, tech, and education niches earn the highest CPM ($10-30+)", "Gaming and entertainment typically earn $1-4 CPM", "US, UK, Canadian and Australian viewers generate the highest ad revenue", "Mid-roll ads in videos 8+ minutes long significantly increase RPM", "December is typically the highest earning month (holiday ad spending)"],
        formula="Daily Earnings = (Daily Views × Monetization Rate × CPM × 0.55) ÷ 1,000<br>Monthly Earnings = Daily Earnings × 30<br>RPM = (Monthly Earnings ÷ Monthly Views) × 1,000",
        table_html='''<h3>YouTube CPM by Niche 2025</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.83rem">
<thead><tr><th>Niche</th><th>Avg CPM</th><th>Avg RPM</th></tr></thead>
<tbody>
<tr><td>Finance / Business</td><td>$15-$50</td><td>$8-$30</td></tr>
<tr><td>Education / Tutorials</td><td>$8-$20</td><td>$5-$12</td></tr>
<tr><td>Technology / Software</td><td>$8-$18</td><td>$4-$10</td></tr>
<tr><td>Health / Fitness</td><td>$6-$12</td><td>$3-$7</td></tr>
<tr><td>General / Lifestyle</td><td>$3-$8</td><td>$1.5-$4</td></tr>
<tr><td>Gaming / Entertainment</td><td>$2-$5</td><td>$1-$3</td></tr>
</tbody></table></div>'''),
    faq_box([
        ("How many views do I need to make $1,000/month on YouTube?",
         "This depends heavily on your niche. For a general/lifestyle channel with $2-3 RPM, you'd need approximately 330,000-500,000 monthly views. For a finance channel with $10 RPM, you'd need only 100,000 views. Most channels at 100K-500K monthly views earn between $300-$5,000/month depending on niche and audience location."),
        ("When can I start monetizing my YouTube channel?",
         "To join the YouTube Partner Program (YPP), you need at least 1,000 subscribers AND 4,000 watch hours in the past 12 months, OR 1,000 subscribers and 10 million Shorts views in 90 days. Once approved, ads are enabled and you can earn AdSense revenue."),
        ("What is the difference between CPM and RPM on YouTube?",
         "CPM (Cost Per Mille) is what advertisers pay YouTube for 1,000 ad impressions. RPM (Revenue Per Mille) is what YOU earn per 1,000 total video views — after YouTube's 45% revenue share and including all monetization sources (ads, memberships, Super Chat, etc.). RPM is always lower than CPM."),
        ("Does YouTube Shorts pay as much as regular videos?",
         "No. YouTube Shorts typically earns $0.03-$0.06 per 1,000 views, which is significantly lower than long-form videos. However, Shorts are excellent for growing subscribers quickly. Most successful creators use Shorts for growth and long-form videos for revenue.")
    ]),
    related_box([
        ("YouTube CPM Calculator","youtube-cpm-calculator.html","&#128200;"),
        ("YouTube RPM Calculator","youtube-rpm-calculator.html","&#128200;"),
        ("YouTube Shorts Earnings","youtube-shorts-earnings-calculator.html","&#127909;"),
        ("YouTube Growth Rate","youtube-growth-rate-calculator.html","&#128200;"),
        ("AdSense RPM Calculator","adsense-rpm-calculator.html","&#128176;"),
        ("Influencer Earnings Per Post","influencer-earnings-per-post-calculator.html","&#128176;"),
    ])
)

CONTENT["youtube-cpm-calculator.html"] = (
    info_box("YouTube CPM Calculator",
        ["CPM (Cost Per Mille) on YouTube refers to the cost advertisers pay for every 1,000 ad impressions on your videos. CPM varies by niche, audience country, time of year, and video content type. Understanding your CPM helps you predict revenue and optimize your content strategy.",
         "Note: CPM is different from RPM. CPM is the gross rate paid by advertisers, while RPM is your actual earnings per 1,000 views after YouTube's revenue share (YouTube keeps 45%)."],
        ["Enter your total ad revenue from YouTube Studio", "Enter the number of ad impressions (not total views)", "Enter total video views for the period", "Click Calculate to see your CPM and RPM breakdown"],
        ["Finance and insurance content commands the highest CPM ($15-50+)", "CPM is always higher than RPM — YouTube takes 45% cut", "Q4 (October-December) has the highest CPM due to holiday advertising budgets", "Ad type affects CPM: skippable ads earn less than non-skippable ones", "Longer videos (8+ min) enable mid-roll ads, boosting effective CPM"]),
    faq_box([
        ("What is a good CPM on YouTube?",
         "A good YouTube CPM varies by niche. Finance channels average $15-50 CPM, technology $8-18, lifestyle $3-8, and gaming $2-5. The global average YouTube CPM is around $4-7. Your audience's country also matters significantly — US, UK, and Canadian viewers generate much higher CPMs than viewers from India or Southeast Asia."),
        ("Why does my YouTube CPM fluctuate so much?",
         "CPM fluctuates due to: advertiser demand (higher in Q4, lower in Q1), audience geography changes, video topic relevance to high-value ads, seasonal trends, and your channel's audience demographics. January and February typically have the lowest CPMs of the year."),
        ("How can I increase my YouTube CPM?",
         "To increase CPM: create content in high-value niches (finance, business, software), target US/UK/Australian audience with relevant content, make videos 8+ minutes long for mid-roll ads, avoid topics that demonetize content (copyright, controversial subjects), and maintain consistent upload schedule to keep advertiser confidence."),
        ("What percentage of YouTube views are monetized?",
         "On average, 40-60% of total views are monetized (have ads shown). Not all views result in ad impressions because: some viewers have ad blockers, some views are from regions with low ad inventory, YouTube Premium subscribers don't see ads, and content may not always be suitable for all advertisers.")
    ]),
    related_box([
        ("YouTube RPM Calculator","youtube-rpm-calculator.html","&#128200;"),
        ("YouTube Money Calculator","youtube-money-calculator.html","&#128176;"),
        ("YouTube Growth Rate","youtube-growth-rate-calculator.html","&#128200;"),
        ("AdSense RPM Calculator","adsense-rpm-calculator.html","&#128176;"),
        ("Affiliate Earnings","affiliate-earnings-calculator.html","&#128200;"),
        ("Website Traffic to Revenue","website-traffic-to-revenue-calculator.html","&#128200;"),
    ])
)

CONTENT["tiktok-earnings-calculator.html"] = (
    info_box("TikTok Earnings Calculator",
        ["TikTok creators can earn money through the TikTok Creator Fund, brand sponsorships, live gifts, and the TikTok Creativity Program (formerly Creator Next). The Creator Fund pays approximately $0.02-$0.04 per 1,000 views, while brand deals are typically far more lucrative.",
         "TikTok's monetization potential depends on your follower count, engagement rate, content niche, and audience demographics. Creators with 100K+ followers in niches like finance, beauty, and education typically earn the most from brand partnerships."],
        ["Enter your average views per TikTok video", "Enter how many videos you post per month", "Add your follower count and engagement rate", "Click Calculate to see Creator Fund income and brand deal estimates"],
        ["TikTok Creator Fund pays less per view than YouTube ($0.02-$0.04 vs $2-10 per 1K views)", "Brand deals on TikTok are typically 3-10x more lucrative than Creator Fund income", "Live gifting can add significant income for creators with engaged communities", "US-based creators earn significantly more from the Creator Fund than international creators", "TikTok's Creativity Program (requires 10K+ followers, 100K+ views/month) pays better than Creator Fund",
         "Finance, business, and educational content earns the highest brand deal rates"],
        table_html='''<h3>TikTok Creator Earnings by Tier 2025</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.83rem">
<thead><tr><th>Followers</th><th>Creator Fund/Month</th><th>Brand Deal/Post</th><th>Total Est.</th></tr></thead>
<tbody>
<tr><td>10K - 50K</td><td>$5 - $50</td><td>$50 - $250</td><td>$100 - $500</td></tr>
<tr><td>50K - 100K</td><td>$50 - $100</td><td>$250 - $800</td><td>$400 - $1,500</td></tr>
<tr><td>100K - 500K</td><td>$100 - $500</td><td>$800 - $3,000</td><td>$1,000 - $6,000</td></tr>
<tr><td>500K - 1M</td><td>$500 - $1,500</td><td>$3,000 - $10,000</td><td>$5,000 - $20,000</td></tr>
<tr><td>1M+</td><td>$1,500+</td><td>$10,000+</td><td>$15,000+/month</td></tr>
</tbody></table></div>'''),
    faq_box([
        ("How many TikTok views do I need to make money?",
         "To join the TikTok Creator Fund, you need at least 10,000 followers and 100,000 views in the past 30 days. However, making significant money from the Creator Fund alone requires millions of views. Most creators focus on brand deals, which can pay $50-$500 per post even with 10K-50K followers."),
        ("Does TikTok pay more than YouTube?",
         "Generally, YouTube pays significantly more per view than TikTok. YouTube RPM averages $2-10+ per 1,000 views, while TikTok Creator Fund pays $0.02-$0.04 per 1,000 views — about 50-100x less. However, TikTok videos can go viral much faster, potentially generating more total views and better brand deal opportunities."),
        ("What is the TikTok Creativity Program?",
         "The TikTok Creativity Program (launched 2023) replaced the original Creator Fund and offers higher per-view payouts. It requires at least 10,000 followers, 100,000+ video views in the last 30 days, videos must be 1+ minute long, and be in an eligible country. Rates are reportedly $0.40-$1.00 per 1,000 views — much higher than the original Creator Fund."),
        ("How do TikTok brand deals work?",
         "Brands pay TikTok creators to feature their products or services in videos. You can find brand deals through: TikTok Creator Marketplace, talent agencies, direct brand outreach, or influencer platforms like AspireIQ. Rates are negotiated based on your follower count, engagement rate, and niche. Most deals include usage rights and exclusivity clauses.")
    ]),
    related_box([
        ("TikTok Engagement Rate","tiktok-engagement-rate-calculator.html","&#127925;"),
        ("TikTok Virality Score","tiktok-virality-score-calculator.html","&#128293;"),
        ("Instagram Influencer Earnings","instagram-influencer-earnings-calculator.html","&#128176;"),
        ("YouTube Money Calculator","youtube-money-calculator.html","&#128176;"),
        ("Brand Deal Rate Calculator","brand-deal-rate-calculator.html","&#129534;"),
        ("Social Media ROI","social-media-roi-calculator.html","&#128200;"),
    ])
)

CONTENT["adsense-rpm-calculator.html"] = (
    info_box("AdSense RPM Calculator",
        ["Google AdSense RPM (Revenue Per Mille) is the estimated earnings you receive for every 1,000 page views on your website. It's the most important metric for blog and website owners to understand their monetization performance.",
         "AdSense RPM is different from CPM. CPM is what advertisers pay; RPM is what you earn after Google's revenue share (Google keeps approximately 32% of ad revenue). Your effective RPM depends on your website niche, audience country, ad placement, and content quality."],
        ["Enter your monthly page views or website traffic", "Enter your AdSense earnings from last month (or use niche estimate)", "Set ads per page to calculate impressions", "Click Calculate to see your RPM, CPM, and monthly/yearly projections"],
        ["Finance, insurance, and legal niches earn $10-25+ RPM", "US, UK, Canadian, and Australian traffic generates the highest RPM", "More ads per page increases total impressions but may reduce UX and RPM", "Content that attracts high-intent buyers (product reviews, how-tos) earns more", "December typically has 30-50% higher RPM due to holiday advertiser spending",
         "Site speed affects ad viewability — faster sites earn more per impression"],
        table_html='''<h3>AdSense RPM by Niche (Global Avg 2025)</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.83rem">
<thead><tr><th>Niche</th><th>RPM Range</th><th>Monthly (100K PV)</th></tr></thead>
<tbody>
<tr><td>Finance / Insurance</td><td>$10-$25</td><td>$1,000-$2,500</td></tr>
<tr><td>Legal / Law</td><td>$8-$20</td><td>$800-$2,000</td></tr>
<tr><td>Technology / Software</td><td>$5-$15</td><td>$500-$1,500</td></tr>
<tr><td>Health / Medical</td><td>$4-$10</td><td>$400-$1,000</td></tr>
<tr><td>General / Lifestyle</td><td>$2-$6</td><td>$200-$600</td></tr>
<tr><td>Entertainment / Gaming</td><td>$1-$4</td><td>$100-$400</td></tr>
</tbody></table></div>'''),
    faq_box([
        ("What is a good AdSense RPM?",
         "A good AdSense RPM depends on your niche and audience. Finance and insurance sites earning $10-25 RPM are considered excellent. Technology blogs at $5-15 RPM are good. General lifestyle or news sites at $2-5 RPM are average. If your RPM is below $1, consider improving content quality, ad placement, or targeting a more profitable niche."),
        ("How can I increase my AdSense RPM?",
         "To increase RPM: create content in high-value niches (finance, legal, health), target US/UK audience with relevant keywords, optimize ad placement (above-fold, in-content ads perform best), ensure your site loads quickly, use auto ads with anchor and vignette ad formats, and focus on long-form content that attracts high-intent readers."),
        ("Why does my AdSense RPM change daily?",
         "AdSense RPM fluctuates daily because: advertiser bidding changes in real-time, your daily traffic mix varies (more US traffic = higher RPM), seasonal advertising budgets shift (higher in Q4, lower in Q1), some days have more relevant advertisers bidding for your content. Monthly averages give a better picture than daily rates."),
        ("How much traffic do I need to make $1,000/month from AdSense?",
         "This depends on your RPM. At $5 RPM (typical lifestyle/general blog), you need 200,000 monthly page views. At $10 RPM (tech/finance), you need 100,000 page views. At $2 RPM (entertainment/gaming), you need 500,000 page views. Most sites need at least 100,000-200,000 monthly visits to earn meaningful AdSense income.")
    ]),
    related_box([
        ("Affiliate Earnings Calculator","affiliate-earnings-calculator.html","&#128200;"),
        ("Website Traffic to Revenue","website-traffic-to-revenue-calculator.html","&#128200;"),
        ("YouTube Money Calculator","youtube-money-calculator.html","&#128176;"),
        ("YouTube RPM Calculator","youtube-rpm-calculator.html","&#128200;"),
        ("Social Media ROI Calculator","social-media-roi-calculator.html","&#128200;"),
        ("Content Performance Score","content-performance-score-calculator.html","&#128202;"),
    ])
)

CONTENT["ai-token-cost-calculator.html"] = (
    info_box("AI Token Cost Calculator",
        ["AI tokens are the basic units of text that large language models (LLMs) like GPT-4o, Claude, and Gemini process. One token is approximately 4 characters or 0.75 words in English. Understanding token costs is critical for businesses and developers building AI-powered applications.",
         "API pricing for AI models is charged per 1 million tokens (input and output separately). Input tokens (your prompts) are typically cheaper than output tokens (the AI's responses). Costs vary significantly between models — from $0.00015/1M tokens for budget models to $15+/1M for premium ones."],
        ["Select your AI model from the dropdown (pre-filled with 2025 pricing)", "Enter your daily API request volume", "Set average input and output tokens per request", "Click Calculate to see daily, monthly, and annual costs"],
        ["1,000 tokens ≈ 750 words ≈ 1.5 pages of text", "Use smaller/cheaper models for simple tasks (GPT-4o mini vs GPT-4o = 30x cost difference)", "Implement prompt caching to reduce costs by up to 90% for repeated system prompts", "Batch processing can reduce costs by 50% on many platforms",
         "Output tokens are typically 2-5x more expensive than input tokens",
         "Always set max_tokens limits to prevent runaway costs"],
        formula="Daily Cost = Requests × (Input Tokens × Input Price/1M + Output Tokens × Output Price/1M)<br>Monthly Cost = Daily Cost × 30<br>Cost per Request = Daily Cost ÷ Daily Requests",
        table_html='''<h3>AI Model Pricing Comparison (2025)</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.83rem">
<thead><tr><th>Model</th><th>Input (per 1M)</th><th>Output (per 1M)</th><th>Best For</th></tr></thead>
<tbody>
<tr><td>GPT-4o mini</td><td>$0.15</td><td>$0.60</td><td>Simple tasks, high volume</td></tr>
<tr><td>GPT-4o</td><td>$5.00</td><td>$15.00</td><td>Complex reasoning, code</td></tr>
<tr><td>Claude 3.5 Sonnet</td><td>$3.00</td><td>$15.00</td><td>Long context, analysis</td></tr>
<tr><td>Claude 3 Haiku</td><td>$0.25</td><td>$1.25</td><td>Fast, affordable tasks</td></tr>
<tr><td>Gemini 1.5 Flash</td><td>$0.35</td><td>$1.05</td><td>Multimodal, speed</td></tr>
<tr><td>Gemini 1.5 Pro</td><td>$3.50</td><td>$10.50</td><td>2M context window</td></tr>
</tbody></table></div>'''),
    faq_box([
        ("How do I reduce my AI API costs?",
         "Key strategies to reduce AI costs: (1) Use smaller models (GPT-4o mini is 30x cheaper than GPT-4o) for simple tasks, (2) Implement prompt caching for repeated system prompts, (3) Set strict max_token limits, (4) Use streaming to stop early when needed, (5) Batch your requests during off-peak hours, (6) Cache responses for identical queries, (7) Compress prompts by removing unnecessary whitespace and instructions."),
        ("What is the difference between input and output tokens?",
         "Input tokens are the tokens in your prompt/message that you send to the AI. Output tokens are the tokens in the AI's generated response. Output tokens are typically 2-5x more expensive because they require more computation to generate. For cost optimization, design prompts that elicit concise responses and use structured output formats."),
        ("How many tokens are in 1,000 words?",
         "As a rule of thumb: 1,000 English words ≈ 1,333 tokens (words × 1.33). Code typically uses more tokens than plain text. Non-English languages (Chinese, Japanese, Korean) often use more tokens per word. OpenAI's Tokenizer tool can help you count exact tokens for your specific use case."),
        ("Which AI model gives the best value for money?",
         "For most production applications, GPT-4o mini or Claude 3 Haiku offer the best value — they're 10-30x cheaper than premium models while handling 80-90% of use cases effectively. Use premium models (GPT-4o, Claude 3.5 Sonnet) only for complex reasoning, legal/medical analysis, or code generation. Start cheap and upgrade only if quality is insufficient.")
    ]),
    related_box([
        ("API Cost Calculator","api-cost-calculator.html","&#128187;"),
        ("SaaS Pricing Calculator","saas-pricing-calculator.html","&#128200;"),
        ("Content Generation Cost","content-generation-cost-calculator.html","&#128221;"),
        ("Website Traffic to Revenue","website-traffic-to-revenue-calculator.html","&#128200;"),
        ("Social Media ROI","social-media-roi-calculator.html","&#128200;"),
        ("Affiliate Earnings","affiliate-earnings-calculator.html","&#128200;"),
    ])
)

# ── CATEGORY-BASED AUTO-GENERATOR ─────────────────────────────────────────

CATEGORY_DATA = {
    "social_instagram": {
        "paras": ["This Instagram calculator helps you track and improve key performance metrics for your Instagram account. Instagram's algorithm rewards accounts with strong, consistent engagement, making it essential to monitor these numbers regularly.",
                  "Whether you're an influencer, brand, or content creator, understanding your Instagram metrics helps you grow your audience, attract sponsorships, and maximize your content's reach."],
        "tips": ["Post consistently — 3-7 times per week is ideal for feed posts", "Reels get 2-3x more organic reach than static feed posts in 2025", "Use 5-15 relevant hashtags (avoid generic ones with billions of posts)", "Post at peak times for your audience (check Instagram Insights)", "Engage with comments within the first 60 minutes after posting"],
        "faq": [
            ("What metrics matter most for Instagram growth?", "The most important Instagram metrics are: engagement rate (likes + comments + saves + shares ÷ followers), reach rate, follower growth rate, and profile visits. Instagram's algorithm prioritizes Reels, so watch time and replay rate are increasingly important. Saves are weighted heavily as they signal long-term content value."),
            ("How often should I post on Instagram?", "For optimal growth, post 3-5 feed posts and 3-7 Reels per week. Stories should be posted daily (3-10 per day). Consistency matters more than frequency — a regular schedule trains the algorithm and your audience. Quality always trumps quantity."),
            ("Does follower count affect Instagram engagement rate?", "Yes, generally as follower count increases, engagement rate decreases. Nano influencers (under 1K) see 5-10%+ ER, while mega influencers (1M+) often see 1-2%. This is why brands increasingly prefer micro and nano influencers for their higher authentic engagement despite smaller audiences."),
            ("How do I see my Instagram analytics?", "Switch to a Creator or Business account to access Instagram Insights. You can view reach, impressions, engagement, follower demographics, and content performance. For deeper analytics, third-party tools like Sprout Social, Hootsuite, or Later provide more detailed reporting.")
        ],
        "related": [("Instagram Engagement Rate","instagram-engagement-rate-calculator.html","&#128247;"),("Instagram Growth Rate","instagram-growth-rate-calculator.html","&#128200;"),("Instagram Influencer Earnings","instagram-influencer-earnings-calculator.html","&#128176;"),("TikTok Engagement Rate","tiktok-engagement-rate-calculator.html","&#127925;"),("Social Media ROI","social-media-roi-calculator.html","&#128200;"),("Virality Score","virality-score-calculator.html","&#128293;")]
    },
    "social_youtube": {
        "paras": ["This YouTube calculator helps you analyze your channel's performance, earnings potential, and growth trajectory. YouTube is the second-largest search engine in the world, making it one of the most powerful platforms for content creators.",
                  "Understanding YouTube metrics like CPM, RPM, retention rate, and subscriber conversion rate helps you make data-driven decisions to grow faster and earn more."],
        "tips": ["YouTube videos 8+ minutes long can include mid-roll ads, significantly increasing RPM", "Thumbnail CTR above 5% is considered good — test different thumbnail styles", "The first 30 seconds of a video are critical — retain viewers early to boost rankings", "Titles with numbers and power words (e.g., 'How to', 'Best', 'Complete Guide') improve CTR", "Consistent upload schedules train the algorithm and subscriber expectations"],
        "faq": [
            ("How does YouTube decide how to rank videos?", "YouTube's algorithm considers: click-through rate (CTR) on thumbnails, average view duration, total watch time, engagement (likes, comments, shares), viewer satisfaction signals, and recency. Videos that keep viewers watching longer are shown to more people through recommendations."),
            ("What is the best time to upload YouTube videos?", "Generally, uploading 2-4 hours before your audience's peak viewing time works best. For most channels targeting US audiences, this means uploading Thursday-Saturday between 12 PM-4 PM EST. Use YouTube Studio analytics to find when your specific audience is most active."),
            ("How long does it take to grow a YouTube channel?", "Most channels take 1-3 years of consistent posting to reach significant size. The average time to reach 1,000 subscribers is 14 months posting weekly. However, viral videos can accelerate this dramatically. Channels posting 3+ times per week typically grow 2-3x faster than those posting once a week."),
            ("Can I monetize YouTube without ads?", "Yes! Beyond AdSense, YouTube creators can earn through: channel memberships (monthly subscriptions), Super Chat and Super Stickers during live streams, merchandise shelf integration, affiliate marketing links, sponsored content deals, and Patreon or other creator platforms.")
        ],
        "related": [("YouTube Money Calculator","youtube-money-calculator.html","&#128176;"),("YouTube CPM Calculator","youtube-cpm-calculator.html","&#128200;"),("YouTube RPM Calculator","youtube-rpm-calculator.html","&#128200;"),("YouTube Watch Time","youtube-watch-time-calculator.html","&#9201;"),("YouTube Growth Rate","youtube-growth-rate-calculator.html","&#128200;"),("AdSense RPM","adsense-rpm-calculator.html","&#128176;")]
    },
    "social_tiktok": {
        "paras": ["This TikTok calculator helps creators and brands measure performance and estimate earnings on the world's fastest-growing social media platform. TikTok's unique algorithm gives even new accounts the chance to go viral, making it one of the best platforms for organic reach in 2025.",
                  "With over 1 billion monthly active users, TikTok offers massive monetization potential through the Creator Fund, Creativity Program, brand partnerships, live gifts, and product promotions."],
        "tips": ["TikTok's algorithm shows your video to a test audience first — high early engagement = wider distribution", "Post 1-3 times daily for maximum growth (TikTok rewards high-frequency posting)", "Use trending sounds and hashtags to increase discovery", "Videos 21-34 seconds get the highest completion rate", "The first 1-3 seconds must hook viewers — front-load your most compelling moment", "Duets, stitches, and reactions help you piggyback on viral content"],
        "faq": [
            ("How does TikTok's algorithm work?", "TikTok's recommendation system (For You Page) analyzes: video completion rate, replay rate, likes, comments, shares, and account performance. Every video gets shown to a small test group first. If engagement is high, it's pushed to a larger audience. This is why new creators can go viral without existing followers."),
            ("What content does well on TikTok?", "Top-performing TikTok content includes: educational and how-to videos (learn something new in 60 seconds), entertainment and humor, trending challenges with original twists, behind-the-scenes content, transformation videos, and storytelling. Authenticity consistently outperforms highly produced content on TikTok."),
            ("How many followers do I need to go live on TikTok?", "You need at least 1,000 followers to go live on TikTok. Going live is a powerful monetization tool — viewers can send you virtual gifts that convert to real money. Top TikTok live streamers can earn thousands of dollars per session from gifts alone."),
            ("Is TikTok available worldwide?", "TikTok is available in 150+ countries and 75 languages. However, the Creator Fund and Creativity Program are only available in select countries (US, UK, Germany, France, Italy, Spain, and a few others). Creators in other countries can still earn through brand deals and live gifts regardless of their location.")
        ],
        "related": [("TikTok Earnings Calculator","tiktok-earnings-calculator.html","&#128176;"),("TikTok Virality Score","tiktok-virality-score-calculator.html","&#128293;"),("TikTok Growth Rate","tiktok-growth-rate-calculator.html","&#128200;"),("Instagram Engagement Rate","instagram-engagement-rate-calculator.html","&#128247;"),("YouTube Money Calculator","youtube-money-calculator.html","&#128176;"),("Micro Influencer Rate","micro-influencer-rate-calculator.html","&#128247;")]
    },
    "social_general": {
        "paras": ["Social media metrics are the key performance indicators that measure how effectively your content connects with your target audience. Tracking these metrics consistently is essential for growing your online presence and maximizing your monetization opportunities.",
                  "Whether you're a brand, content creator, or marketer, understanding your social media performance data helps you optimize your strategy, identify what content resonates, and demonstrate ROI to clients or stakeholders."],
        "tips": ["Track metrics consistently over time — weekly snapshots give better insight than single measurements", "Engagement rate is more valuable than raw follower count for brand deals", "Set specific, measurable goals before creating content (e.g., 5% ER, 10% monthly growth)", "Analyze your best-performing content to identify patterns and replicate success", "Benchmark your metrics against competitors in your niche for context"],
        "faq": [
            ("Why should I track social media metrics?", "Tracking social media metrics helps you understand what content works, who your audience is, when they're most active, and how to grow effectively. It also helps you justify your value to brands, optimize your content strategy, and identify problems early (like declining engagement) before they become serious."),
            ("What is the difference between reach and impressions?", "Reach is the number of unique accounts that saw your content. Impressions is the total number of times your content was displayed (including multiple views by the same person). A post with 1,000 reach and 1,500 impressions means 500 people viewed it more than once."),
            ("How often should I review my social media analytics?", "Review weekly for trend identification, monthly for strategy adjustments, and quarterly for comprehensive performance reviews. Daily checks can cause 'metric anxiety' from normal fluctuations. Focus on 30-90 day trends rather than day-to-day variations."),
            ("What tools help track social media performance?", "Free tools: Meta Business Suite (Facebook/Instagram), TikTok Studio, YouTube Studio. Paid tools: Sprout Social, Hootsuite, Later, Buffer, Brandwatch. For influencers, Klear, HypeAuditor, and Modash provide detailed audience analytics including authenticity scores.")
        ],
        "related": [("Instagram Engagement Rate","instagram-engagement-rate-calculator.html","&#128247;"),("YouTube Money Calculator","youtube-money-calculator.html","&#128176;"),("TikTok Earnings","tiktok-earnings-calculator.html","&#127925;"),("Social Media ROI","social-media-roi-calculator.html","&#128200;"),("Influencer Earnings","influencer-earnings-per-post-calculator.html","&#128176;"),("Virality Score","virality-score-calculator.html","&#128293;")]
    },
    "finance": {
        "paras": ["Financial calculators help you make informed money decisions by running complex calculations instantly. From investments to loans, taxes to savings, having accurate financial projections is key to achieving your financial goals.",
                  "Using this calculator, you can quickly model different scenarios to find the best financial strategy for your specific situation."],
        "tips": ["Always compare multiple scenarios before making major financial decisions", "Account for inflation when projecting long-term returns (typically 6-7% nominal - 3% inflation = 3-4% real return)", "Tax implications significantly affect actual returns — consider post-tax calculations", "Emergency fund (3-6 months expenses) should be established before investing", "Diversification reduces risk without necessarily reducing expected returns"],
        "faq": [
            ("How accurate are online financial calculators?", "Online financial calculators provide estimates based on the inputs you provide and standard financial formulas. They're highly accurate for fixed scenarios but cannot account for market volatility, tax law changes, or unexpected events. Use them as planning tools rather than guaranteed projections."),
            ("Should I pay off debt or invest first?", "The standard advice: if your debt interest rate is higher than your expected investment return, pay off debt first. Credit card debt (18-24%) should almost always be paid first. If your debt rate is low (below 6-7%), investing simultaneously may make mathematical sense. Emergency fund always comes first."),
            ("What is the rule of 72?", "The Rule of 72 is a quick way to estimate how long it takes to double your money. Divide 72 by your annual interest rate. Example: at 8% annual return, your money doubles in 72÷8 = 9 years. At 6%, it doubles in 12 years. This works well for rates between 5-15%."),
            ("How much should I save each month?", "Financial experts recommend saving at least 20% of your income (50/30/20 rule: 50% needs, 30% wants, 20% savings/debt). For retirement, aim to save 15% of gross income. Start with what you can — even 5-10% is better than nothing and can be increased over time.")
        ],
        "related": [("EMI Calculator","emi-calculator.html","&#127968;"),("SIP Calculator","sip-calculator.html","&#128200;"),("Compound Interest","compound-interest-calculator.html","&#128185;"),("Income Tax","income-tax-calculator.html","&#129534;"),("GST Calculator","gst-calculator.html","&#128202;"),("ROI Calculator","roi-calculator.html","&#128202;")]
    },
    "health": {
        "paras": ["Health and fitness calculators provide evidence-based measurements to help you track your wellness journey. These tools use scientifically validated formulas to give you accurate insights into your health metrics.",
                  "Always remember that calculators provide estimates based on population averages. Individual results may vary, and for medical decisions, always consult a qualified healthcare professional."],
        "tips": ["Track your metrics monthly rather than daily to see meaningful trends", "Multiple measurements (BMI + body fat % + waist circumference) give a more complete health picture than a single number", "Healthy habits matter more than perfect numbers — consistency is key", "Hydration, sleep, and stress management are as important as diet and exercise", "Set SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound) for best results"],
        "faq": [
            ("Are online health calculators medically accurate?", "Health calculators use established medical formulas and population-based research. They provide good general estimates but aren't substitutes for professional medical assessment. BMI, for example, doesn't account for muscle mass, bone density, or body composition. Use calculators as starting points for health awareness."),
            ("How often should I track my health metrics?", "For weight and BMI, weekly measurements at the same time and conditions give the most consistent data. Monthly measurements are sufficient for body composition changes. Daily fluctuations (1-3 kg) are normal due to water retention, food, and clothing. Focus on monthly trends."),
            ("What should I do if my health metrics are outside normal range?", "If your health metrics indicate risk (high BMI, abnormal blood pressure, concerning calorie deficit), consult a healthcare provider before making significant lifestyle changes. A doctor can order proper diagnostic tests and provide personalized guidance based on your complete health picture."),
            ("How are these health formulas calculated?", "Health formulas like BMI, BMR, and body fat percentage are derived from large-scale population studies and validated by medical research. While they may not be perfect for every individual (especially athletes or older adults), they're the best validated tools available for population-level health assessment.")
        ],
        "related": [("BMI Calculator","bmi-calculator.html","&#9878;"),("BMR Calculator","bmr-calculator.html","&#128293;"),("Calorie Calculator","calorie-calculator.html","&#127822;"),("Protein Calculator","protein-calculator.html","&#129385;"),("Body Fat Calculator","body-fat-calculator.html","&#128208;"),("Water Intake","water-intake-calculator.html","&#128167;")]
    },
    "math": {
        "paras": ["Mathematical calculators provide instant, accurate solutions to complex calculations that would otherwise take significant time and effort. These tools are essential for students, engineers, scientists, and professionals.",
                  "Whether you're solving equations, converting units, or performing statistical analysis, our calculators use verified mathematical formulas to deliver precise results."],
        "tips": ["Double-check inputs carefully — garbage in, garbage out applies to all calculators", "For complex calculations, break the problem into smaller steps", "Always verify results against known benchmarks when possible", "Understanding the formula behind the calculation helps you spot errors", "Use significant figures appropriate to your data's precision"],
        "faq": [
            ("Why do online calculators sometimes give different answers?", "Differences can occur due to: rounding at different stages of calculation, different formula interpretations, significant figure handling, and edge case assumptions. For critical calculations, always cross-check with at least one other source or method."),
            ("What is the order of operations?", "The order of operations is PEMDAS/BODMAS: Parentheses/Brackets, Exponents/Orders, Multiplication and Division (left to right), Addition and Subtraction (left to right). This universal rule ensures mathematical expressions have one correct interpretation."),
            ("How do I know if my calculation result is reasonable?", "Use estimation to sanity-check results. Round numbers and do a quick mental calculation. If your precise answer is wildly different from your estimate, recheck the inputs. Dimensional analysis (checking that units work out correctly) is also very useful for catching errors."),
            ("Are there limitations to calculator accuracy?", "Yes. Calculators use floating-point arithmetic which can introduce tiny rounding errors in complex calculations. For most practical purposes, these are negligible. However, for financial, scientific, or engineering calculations requiring high precision, specialized tools may be needed.")
        ],
        "related": [("Percentage Calculator","percentage-calculator.html","&#128290;"),("Age Calculator","age-calculator.html","&#127874;"),("Scientific Calculator","scientific-calculator.html","&#129518;"),("Square Root Calculator","square-root-calculator.html","&#8730;"),("Statistics Calculator","statistics-calculator.html","&#128202;"),("Unit Converter","unit-converter.html","&#128208;")]
    },
    "ai": {
        "paras": ["AI and technology cost calculators help developers, product managers, and businesses estimate and optimize their spending on AI APIs, software-as-a-service tools, and technology infrastructure.",
                  "With AI API costs varying dramatically between models and providers, and usage scaling quickly with product growth, accurate cost modeling is essential for sustainable AI product development."],
        "tips": ["Always test with the cheapest model first (GPT-4o mini, Claude Haiku) and only upgrade if quality is insufficient", "Implement response caching to avoid paying for identical prompts", "Use streaming to stop generation early when you have enough output", "Monitor token usage daily — costs can scale unexpectedly with user growth", "Consider model distillation: use GPT-4o to generate training data for fine-tuning cheaper models"],
        "faq": [
            ("How do I budget for AI API costs?", "Start by estimating your requests per day and average tokens per request. Multiply by the model's cost per token. Add 30% buffer for growth and variability. Most early-stage products spend $50-500/month on AI APIs. Set billing alerts at 50%, 80%, and 100% of your budget in your provider's console."),
            ("What is the cheapest AI model for production use?", "For most production tasks, GPT-4o mini ($0.15/$0.60 per 1M in/out tokens) or Claude 3 Haiku ($0.25/$1.25) offer the best cost-performance balance. Gemini 1.5 Flash is also very cost-effective. Open-source models hosted locally (Llama 3, Mistral) can be even cheaper but require infrastructure investment."),
            ("How can I reduce AI costs as I scale?", "As you scale: (1) Implement semantic caching (cache similar, not just identical, requests), (2) Use smaller models for simple subtasks, (3) Batch non-urgent requests, (4) Fine-tune smaller models on your specific use case using GPT-4o generated data, (5) Negotiate enterprise pricing with providers at significant volume."),
            ("Is it better to use OpenAI or build with open-source models?", "OpenAI/Anthropic/Google APIs are best for quick deployment, no infrastructure overhead, and when performance is critical. Open-source models (Llama 3, Mistral) are better for cost at scale, data privacy requirements, offline use, and complete customization control. Most companies use both depending on the use case.")
        ],
        "related": [("AI Token Cost Calculator","ai-token-cost-calculator.html","&#129302;"),("API Cost Calculator","api-cost-calculator.html","&#128187;"),("SaaS Pricing Calculator","saas-pricing-calculator.html","&#128200;"),("Content Generation Cost","content-generation-cost-calculator.html","&#128221;"),("AdSense RPM Calculator","adsense-rpm-calculator.html","&#128176;"),("Affiliate Earnings","affiliate-earnings-calculator.html","&#128200;")]
    },
    "construction": {
        "paras": ["Construction and home improvement calculators help homeowners, contractors, and DIY enthusiasts accurately estimate materials and costs before starting projects. Accurate material estimation prevents costly overbuying or frustrating shortages mid-project.",
                  "These calculators use standard construction formulas to give you reliable estimates. Always add a 10-15% waste factor to material quantities to account for cuts, mistakes, and breakage."],
        "tips": ["Always add 10-15% extra to material orders for waste and breakage", "Measure twice, cut once — accurate measurements save money and time", "Consider material delivery costs when budgeting (can add 10-20% to material costs)", "Check local building codes before starting any structural project", "Get at least 3 contractor quotes for large projects to ensure fair pricing"],
        "faq": [
            ("How much should I add for waste factor in construction?", "Standard waste factors by material: Tile/flooring: 10-15% extra. Paint: 10% for one coat. Lumber: 10-15%. Brick/block: 5-10%. Roofing shingles: 10-15%. For complex patterns, irregular shapes, or less experienced DIYers, add an additional 5%."),
            ("How do I calculate square footage for a room?", "For a rectangular room, multiply length × width. For L-shaped rooms, divide into rectangles and add areas. For circular spaces, use π × radius². For irregular shapes, divide into simple geometric shapes and sum them. Always measure at the widest points."),
            ("Should I do DIY or hire a contractor?", "DIY is suitable for painting, minor repairs, flooring installation, and simple landscaping if you have the skills and tools. Hire professionals for electrical work, plumbing, structural changes, roofing, and anything requiring permits. Compare DIY cost (materials + your time at hourly rate) vs contractor quote."),
            ("How do I estimate labor costs for construction?", "Labor is typically 40-60% of total project cost. As a rough guide: general contractor markup is 15-25% above subcontractor costs. Labor rates vary widely by region — US averages: carpenter $50-100/hr, electrician $50-100/hr, plumber $45-200/hr, painter $20-50/hr. Get multiple quotes.")
        ],
        "related": [("Square Footage Calculator","square-footage-calculator.html","&#127968;"),("Paint Calculator","paint-calculator.html","&#127912;"),("Tile Calculator","tile-calculator.html","&#127968;"),("Concrete Calculator","concrete-calculator.html","&#127959;"),("Roof Pitch Calculator","roof-pitch-calculator.html","&#127968;"),("Flooring Calculator","flooring-calculator.html","&#127968;")]
    },
    "convert": {
        "paras": ["Unit converters help you quickly and accurately convert between different measurement systems used worldwide. Whether you need to convert metric to imperial, or between scientific units, accurate conversions are essential in science, engineering, cooking, and everyday life.",
                  "These converters use exact conversion factors from international standards (SI units, ISO definitions) to ensure maximum accuracy."],
        "tips": ["The metric system (SI units) is used by 95% of the world — learning key conversions helps in international contexts", "Temperature conversions: °C to °F: multiply by 9/5 then add 32", "For cooking: 1 cup = 240 mL, 1 tablespoon = 15 mL, 1 teaspoon = 5 mL", "1 mile = 1.60934 km, 1 kg = 2.20462 lbs, 1 inch = 2.54 cm", "When precision matters, use the exact conversion factor, not a rounded approximation"],
        "faq": [
            ("What is the metric system?", "The metric system (International System of Units or SI) is the globally standard system of measurement. It's based on multiples of 10, making calculations straightforward. Used by scientists worldwide and by most countries for everyday measurements. The US is one of only three countries (with Myanmar and Liberia) not officially using metric."),
            ("How do I remember conversion factors?", "Key tricks: 'King Henry Died By Drinking Cold Milk' for kilo-hecto-deca-base-deci-centi-milli. For temp: 'Multiply by 2 and add 30' gives a quick Celsius-to-Fahrenheit approximation (exact: ×1.8 + 32). For km to miles, multiply by 0.6 (exact: ×0.621371)."),
            ("Why does the US still use imperial units?", "The US officially adopted the metric system in 1866 but never mandated its use in daily life. Switching would require updating infrastructure, education, and cultural habits at enormous cost. However, US science, medicine, military, and international trade widely use metric. The Metric Conversion Act of 1975 made metric the preferred system."),
            ("What's the most common conversion mistake?", "The most common mistake is confusing mass and weight (kilograms vs. pounds), especially for international shipping. Also: confusing fluid ounces (volume) with ounces (weight), and using the wrong temperature scale (°C vs °F). Always specify units in international communications.")
        ],
        "related": [("Unit Converter","unit-converter.html","&#128208;"),("Temperature Converter","temperature-converter.html","&#127777;"),("Length Converter","length-converter.html","&#128208;"),("Weight Converter","weight-converter.html","&#9878;"),("Speed Converter","speed-converter.html","&#128663;"),("Energy Converter","energy-converter.html","&#9889;")]
    },
    "datetime": {
        "paras": ["Date and time calculators help you compute the difference between dates, add or subtract time periods, and plan around specific dates. These tools are invaluable for project management, event planning, age calculation, and deadline tracking.",
                  "All calculations account for leap years, varying month lengths, and timezone considerations for accurate results."],
        "tips": ["Leap years occur every 4 years (divisible by 4), except for years divisible by 100, unless also divisible by 400", "Time zone differences can shift event dates — always specify timezone for international planning", "Working days calculators exclude weekends; for accurate business deadlines, also subtract public holidays", "The ISO 8601 date format (YYYY-MM-DD) is the international standard and avoids DD/MM vs MM/DD confusion"],
        "faq": [
            ("How do leap years affect date calculations?", "Leap years add an extra day (February 29) every 4 years, making that year 366 days. This matters for anniversary calculations, age calculations around late February birthdays, and any calculation spanning multiple years. Years divisible by 100 skip leap year UNLESS also divisible by 400 (e.g., 2000 was a leap year, 1900 was not)."),
            ("What is the difference between calendar days and business days?", "Calendar days count every day including weekends and holidays. Business days (also called working days) count only Monday-Friday, excluding weekends. Some countries also exclude national public holidays. For financial and legal deadlines, whether 'days' means calendar or business days is critically important."),
            ("How accurate are online date calculators?", "Date calculators are extremely accurate for standard Gregorian calendar calculations. The main variable is whether to include/exclude the start and end dates in the count. Different contexts use different conventions — courts often use 'counting from the day after' while age calculations typically use 'from the birthday itself'."),
            ("What is Unix timestamp?", "A Unix timestamp (also called POSIX time or Epoch time) counts the number of seconds elapsed since January 1, 1970, 00:00:00 UTC. It's the standard way computers store and transmit date/time information. Converting between Unix timestamps and human-readable dates is a common programming task.")
        ],
        "related": [("Age Calculator","age-calculator.html","&#127874;"),("Date Calculator","date-calculator.html","&#128197;"),("Days Until Calculator","days-until-calculator.html","&#128197;"),("Working Days Calculator","working-days-calculator.html","&#128197;"),("Time Zone Converter","time-zone-converter.html","&#127760;"),("Add Days Calculator","add-days-calculator.html","&#128197;")]
    },
    "education": {
        "paras": ["Academic calculators help students, educators, and parents track academic performance, plan study schedules, and understand grading systems across different educational institutions.",
                  "Whether you're calculating GPA, grade percentages, or planning how many study hours you need, these tools help you stay on track academically."],
        "tips": ["Most US universities require a GPA of 2.0+ to maintain good academic standing", "Weighted GPA (considering AP/IB courses) is often more relevant for college admissions than unweighted GPA", "Consistent studying (1-2 hours daily) beats marathon cramming sessions for long-term retention", "A 1% daily improvement compounds — studying 1% better each day leads to 37x improvement over a year"],
        "faq": [
            ("What is a good GPA?", "GPA scales vary by institution. On a 4.0 scale: 3.7-4.0 = Excellent (A range), 3.0-3.6 = Good (B+ to A-), 2.0-2.9 = Average (C to B), below 2.0 may risk academic probation. For university admissions, competitive schools typically look for 3.5+ unweighted GPA. Graduate school admissions often require 3.0-3.5+."),
            ("How is percentage converted to GPA?", "In the US 4.0 scale: 93-100% = 4.0 (A), 90-92% = 3.7 (A-), 87-89% = 3.3 (B+), 83-86% = 3.0 (B), 80-82% = 2.7 (B-), 77-79% = 2.3 (C+), 73-76% = 2.0 (C). Indian system: CGPA × 9.5 ≈ percentage (for most universities using 10-point CGPA scale)."),
            ("How many study hours per day is optimal?", "Research suggests 3-5 focused study hours per day for students is optimal. The Pomodoro Technique (25 min study + 5 min break, repeated 4 times, then 30 min break) helps maintain concentration. Quality matters more than quantity — eliminate distractions during study sessions for maximum effectiveness."),
            ("What is the difference between CGPA and GPA?", "GPA (Grade Point Average) is calculated for a specific term/semester. CGPA (Cumulative GPA) is the average across all terms completed to date. CGPA provides a comprehensive view of academic performance over time, while GPA shows current semester performance. Most Indian universities use CGPA on a 10-point scale.")
        ],
        "related": [("GPA Calculator","gpa-calculator.html","&#127891;"),("Grade Calculator","grade-calculator.html","&#127891;"),("CGPA to Percentage","cgpa-to-percentage-calculator.html","&#127891;"),("Study Hours Calculator","study-hours-calculator.html","&#128218;"),("Percentage Calculator","percentage-calculator.html","&#128290;"),("Reading Time Calculator","reading-time-calculator.html","&#128218;")]
    },
    "travel": {
        "paras": ["Travel and fuel calculators help you plan trips efficiently by estimating fuel costs, travel times, and budgets. Whether planning a road trip or calculating mileage reimbursement, accurate travel calculations help you budget and plan effectively.",
                  "These calculators help you compare travel options, optimize routes for fuel efficiency, and track transportation expenses."],
        "tips": ["Regular vehicle maintenance improves fuel efficiency by up to 15%", "Optimal highway speed for fuel efficiency is typically 55-65 mph (88-104 km/h)", "Tire pressure affects fuel economy — properly inflated tires improve MPG by 0.5-3%", "Carpooling can cut per-person fuel costs dramatically while reducing carbon footprint", "Gas prices vary significantly by location — apps like GasBuddy help find the cheapest fuel nearby"],
        "faq": [
            ("How do I calculate fuel cost for a road trip?", "Formula: Trip Cost = (Distance ÷ Fuel Efficiency) × Fuel Price. Example: 500 miles, 30 MPG, $3.50/gallon = (500÷30) × $3.50 = $58.33 in fuel. Add 10% for extra driving (detours, traffic) and divide by number of passengers for per-person cost."),
            ("What affects vehicle fuel efficiency?", "Key factors: driving speed (efficiency peaks at 55-65 mph), acceleration patterns (smooth acceleration saves fuel), air conditioning usage (increases consumption 5-25%), tire pressure, vehicle load weight, route type (highway vs city), vehicle maintenance condition, and weather (cold reduces efficiency 10-20%)."),
            ("What is the IRS standard mileage rate?", "The IRS standard mileage rate for 2025 is 67 cents per mile for business use of a personal vehicle. This rate is used to calculate tax deductions for business travel or reimbursements. The rate is adjusted annually and may change mid-year during extraordinary fuel price changes."),
            ("How do I calculate carbon footprint for travel?", "Average car CO2 emissions: 0.21 kg CO2 per kilometer (small car), 0.27 kg/km (medium), 0.35 kg/km (large SUV). Flying emits approximately 0.255 kg CO2 per passenger per km (economy class). Train travel averages 0.041 kg CO2/km, making it 6x more environmentally friendly than flying.")
        ],
        "related": [("Fuel Cost Calculator","fuel-cost-calculator.html","&#9981;"),("Fuel Efficiency Calculator","fuel-efficiency-calculator.html","&#128663;"),("Carbon Footprint","carbon-footprint-calculator.html","&#127807;"),("Tip Calculator","tip-calculator.html","&#128176;"),("Currency Converter","currency-converter.html","&#128178;"),("Travel Budget","travel-budget-calculator.html","&#9992;")]
    },
    "default": {
        "paras": ["This calculator provides instant, accurate calculations to help you make better decisions. Built with the latest standards and best practices, it delivers reliable results for everyday use.",
                  "Simply enter your values, click calculate, and get precise results instantly. Share your results or use the copy function to save them for later reference."],
        "tips": ["Enter values carefully — results are only as accurate as your inputs", "Use the copy button to save your results for reference", "Bookmark this page for quick access next time", "Share results with the WhatsApp button for easy collaboration"],
        "faq": [
            ("How accurate is this calculator?", "This calculator uses standard mathematical formulas and provides results accurate to standard precision. For critical financial or medical decisions, always verify with a professional. The formulas are based on widely accepted industry standards."),
            ("Can I use this on my mobile phone?", "Yes! This calculator is fully responsive and works on all devices — smartphones, tablets, and desktops. No app download required. Simply open the page in your mobile browser for instant access."),
            ("Is this calculator free to use?", "Yes, completely free with no registration required. SuperCalc provides all calculators free of charge for personal and commercial use."),
            ("How do I share my calculation results?", "Use the Share button to share via WhatsApp, or the Copy button to copy results to clipboard. You can also print results using the Print button for physical records.")
        ],
        "related": [("EMI Calculator","emi-calculator.html","&#127968;"),("BMI Calculator","bmi-calculator.html","&#9878;"),("Percentage Calculator","percentage-calculator.html","&#128290;"),("Age Calculator","age-calculator.html","&#127874;"),("GST Calculator","gst-calculator.html","&#128202;"),("SIP Calculator","sip-calculator.html","&#128200;")]
    }
}


def detect_category(filename):
    f = filename.lower()
    if any(k in f for k in ["instagram"]): return "social_instagram"
    if any(k in f for k in ["youtube", "views-to-sub"]): return "social_youtube"
    if any(k in f for k in ["tiktok"]): return "social_tiktok"
    if any(k in f for k in ["twitter","tweet","linkedin","influencer","brand-deal","adsense","affiliate","social-media","website-traffic","follower","micro-influencer","virality","content-performance","post-frequency","engagement-to","engagement-ratio"]): return "social_general"
    if any(k in f for k in ["ai-token","api-cost","saas","content-generation"]): return "ai"
    if any(k in f for k in ["emi","sip","fd-","rd-","ppf","gst","tax","salary","loan","mortgage","investment","finance","savings","retirement","profit","roi","inflation","currency","dividend","stock","debt","budget","payroll","lease","margin","markup","gold","property","hra","gratuity","nps","mutual","compound","simple-interest","discount","credit-card","net-worth","net-pay","break-even","freelancer","capital-gains","depreciation","bond","options","apy","down-payment","childbirth","college-cost","customer-ltv","employee-cost","invoice","food-cost","mileage","rent-vs-buy"]): return "finance"
    if any(k in f for k in ["bmi","bmr","calorie","tdee","weight","protein","water-intake","pregnancy","ovulation","heart-rate","running","macro","sleep","one-rep","waist","blood","alcohol","step-counter","life-expect","vo2","body-fat","army","lean","menstrual","vitamin","hydration","bac","dose","swimming","cycling","walking","yoga","surface-area","pace"]): return "health"
    if any(k in f for k in ["tile","paint","concrete","brick","floor","roof","stair","fence","mulch","gravel","drywall","square-footage","land-area","electricity","solar","power-unit","pipe-flow","electricity-saving"]): return "construction"
    if any(k in f for k in ["converter","convert","celsius","fahrenheit","km","mph","liter","gallon","kg","pound","inch","meter","unit-","data-","digital-storage","angle","speed-","length-","weight-","temperature-","energy-","pressure-","cooking-","time-unit","force-","power-unit","currency-inflation","specific-gravity"]): return "convert"
    if any(k in f for k in ["date","time","age-diff","days-until","working-days","countdown","anniversary","week-number","birth-year","planet","add-days"]): return "datetime"
    if any(k in f for k in ["gpa","grade","cgpa","study","reading-time","word-count","exam","percentage-change","percentage-off"]): return "education"
    if any(k in f for k in ["fuel","flight","travel","tip-","bill-split","carbon-footprint","water-footprint","mileage-reimb","nautical","engine-disp","horsepower"]): return "travel"
    if any(k in f for k in ["percentage","age-calc","scientific","fraction","square-root","exponent","lcm","average","statistics","quadratic","trigon","matrix","logarithm","factorial","prime","binary","standard-dev","half-life","molarity","density","kinetic","ohm","ph","wavelength","number-","roman-","number-system","z-score","acceleration","wind-chill"]): return "math"
    return "default"


def get_details(filename, title):
    if filename in CONTENT:
        return CONTENT[filename]
    cat = detect_category(filename)
    data = CATEGORY_DATA.get(cat, CATEGORY_DATA["default"])
    info = info_box(
        title,
        data["paras"],
        tips=data["tips"]
    )
    faqs = faq_box(data["faq"])
    rel = related_box(data["related"])
    return (info, faqs, rel)


def process_page(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has info-box
    if 'class="info-box"' in html or "info-box" in html:
        return False

    # Extract title from <h1> or <title>
    title_match = re.search(r'<h1[^>]*>.*?([A-Za-z][^<&]{5,60})</h1>', html)
    if title_match:
        title = re.sub(r'&#\d+;|&[a-z]+;|<[^>]+>', '', title_match.group(1)).strip()
    else:
        title_match = re.search(r'<title>([^|<]+)', html)
        title = title_match.group(1).strip() if title_match else filename.replace('-', ' ').replace('.html', '').title()

    # Clean title
    title = re.sub(r'SuperCalc.*', '', title).strip(' |').strip()
    if not title: title = filename.replace('-', ' ').replace('.html', '').title()

    info, faqs, rel = get_details(filename, title)
    new_content = '\n' + info + faqs + rel

    # Find injection point: before the col-lg-8 closing </div>
    # Pattern: </div>\r?\n    <div class="col-lg-4">
    pattern = r'(</div>)\s*\r?\n(\s+<div class="col-lg-4">)'
    
    # Find the LAST match
    matches = list(re.finditer(pattern, html))
    if not matches:
        return False

    last_match = matches[-1]
    insert_pos = last_match.start(1)  # Position of last </div>
    html = html[:insert_pos] + new_content + html[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return True


# ── PROCESS ALL THIN PAGES ────────────────────────────────────────────────

skip_files = {'about.html', 'privacy.html', 'terms.html', 'index.html'}
processed = 0
skipped = 0
errors = []

html_files = sorted([f for f in os.listdir(BASE) if f.endswith('.html') and f not in skip_files])

for filename in html_files:
    filepath = os.path.join(BASE, filename)
    try:
        if process_page(filepath):
            processed += 1
            if processed % 20 == 0:
                print(f"  Progress: {processed} pages enhanced...")
        else:
            skipped += 1
    except Exception as e:
        errors.append(f"{filename}: {e}")

print(f"\n=== Complete ===")
print(f"Enhanced: {processed} pages")
print(f"Skipped (already detailed): {skipped} pages")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors[:10]: print(f"  {e}")
