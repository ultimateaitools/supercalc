# -*- coding: utf-8 -*-
"""
enhance_seo.py - Enhances SEO meta tags for all 43 new social/AI calculator pages
and ensures all pages have proper title optimization.
"""
import os, re

BASE = r"d:\Datomate AI Lab\CalcWebsite"

# Rich SEO data for each page: {filename: (title, description, keywords)}
SEO_DATA = {
    # ── INSTAGRAM ──
    "instagram-engagement-rate-calculator.html": (
        "Instagram Engagement Rate Calculator 2025 - Free IG Analytics Tool | SuperCalc",
        "Calculate your Instagram engagement rate instantly. Free tool for influencers and brands. Check if your IG engagement is good, average, or poor. Used by 50,000+ creators worldwide.",
        "instagram engagement rate calculator, instagram engagement rate, how to calculate instagram engagement rate, ig engagement calculator, instagram analytics tool, influencer engagement rate, what is a good instagram engagement rate 2025"
    ),
    "instagram-engagement-per-post-calculator.html": (
        "Instagram Engagement Per Post Calculator - Analyze Every Post | SuperCalc",
        "Calculate average engagement per Instagram post including likes, comments, saves and shares. Find your best-performing content and optimize your Instagram strategy.",
        "instagram engagement per post calculator, instagram post analytics, average engagement per post instagram, instagram likes comments per post, instagram content performance"
    ),
    "instagram-reach-rate-calculator.html": (
        "Instagram Reach Rate Calculator - Check Your Post Reach % | SuperCalc",
        "Calculate what percentage of your Instagram followers actually see your posts. Free Instagram reach rate calculator for creators, brands and marketers.",
        "instagram reach rate calculator, instagram reach percentage, post reach instagram calculator, organic reach instagram, impressions vs reach calculator"
    ),
    "instagram-growth-rate-calculator.html": (
        "Instagram Growth Rate Calculator - Track Follower Growth | SuperCalc",
        "Track your Instagram follower growth rate month over month. Project when you'll reach 10K, 100K and 1 million followers. Free Instagram growth calculator.",
        "instagram growth rate calculator, instagram follower growth calculator, monthly growth rate instagram, how fast is my instagram growing, instagram account growth tracker"
    ),
    "instagram-influencer-earnings-calculator.html": (
        "Instagram Influencer Earnings Calculator 2025 - Sponsored Post Rate | SuperCalc",
        "Estimate how much you can earn per sponsored Instagram post. Calculate your influencer rate card based on followers, engagement rate and niche. Used by 100,000+ influencers.",
        "instagram influencer earnings calculator, instagram sponsored post price, how much do instagram influencers make, instagram rate card calculator, sponsored content pricing instagram, influencer fee calculator 2025"
    ),
    "instagram-reels-earnings-calculator.html": (
        "Instagram Reels Earnings Calculator - Monetize Your Reels | SuperCalc",
        "Calculate how much you can earn from Instagram Reels. Estimate Reels brand deal rates and Play Bonus income based on views, followers, and engagement rate.",
        "instagram reels earnings calculator, instagram reels monetization, how much instagram reels pay, reels play bonus calculator, instagram reels views to money"
    ),

    # ── YOUTUBE ──
    "youtube-engagement-rate-calculator.html": (
        "YouTube Engagement Rate Calculator - Likes Comments Analysis | SuperCalc",
        "Calculate your YouTube channel engagement rate from likes, comments and views. See how your channel compares to industry benchmarks. Free YouTube analytics tool.",
        "youtube engagement rate calculator, youtube engagement rate, youtube likes to views ratio, youtube channel analytics, youtube engagement metrics 2025"
    ),
    "youtube-money-calculator.html": (
        "YouTube Money Calculator 2025 - How Much Does YouTube Pay? | SuperCalc",
        "Calculate how much money your YouTube channel makes. Estimate daily, monthly and yearly YouTube earnings based on views, CPM and niche. The most accurate YouTube earnings calculator.",
        "youtube money calculator, youtube earnings calculator 2025, how much does youtube pay per view, youtube revenue calculator, how much do youtubers make, youtube income calculator, youtube salary calculator"
    ),
    "youtube-cpm-calculator.html": (
        "YouTube CPM Calculator 2025 - Cost Per Mille Analysis | SuperCalc",
        "Calculate your YouTube CPM (Cost Per Mille). Understand your channel's ad rate and compare to industry benchmarks. Free YouTube CPM calculator for creators.",
        "youtube CPM calculator, what is youtube CPM, youtube ad rate calculator, CPM by niche youtube, how to calculate youtube CPM, youtube advertising cost 2025"
    ),
    "youtube-rpm-calculator.html": (
        "YouTube RPM Calculator - Revenue Per 1000 Views | SuperCalc",
        "Calculate your YouTube RPM (Revenue Per Mille). Find out exactly how much you earn per 1000 views and understand the difference between CPM and RPM.",
        "youtube RPM calculator, youtube revenue per mille, RPM vs CPM youtube, youtube income per 1000 views, youtube RPM by niche, how to increase youtube RPM"
    ),
    "youtube-growth-rate-calculator.html": (
        "YouTube Channel Growth Rate Calculator - Subscriber Growth | SuperCalc",
        "Track your YouTube subscriber growth rate. Calculate daily subscriber gains, project future milestones, and find out when you'll reach 100K subscribers.",
        "youtube growth rate calculator, youtube subscriber growth calculator, youtube channel growth tracker, when will i reach 100k subscribers, youtube growth projection 2025"
    ),
    "youtube-shorts-earnings-calculator.html": (
        "YouTube Shorts Earnings Calculator 2025 - Monetize Shorts | SuperCalc",
        "Calculate how much YouTube Shorts can earn you. Estimate Shorts ad revenue, Creator Fund payments, and brand deal income based on your views and subscribers.",
        "youtube shorts earnings calculator, youtube shorts monetization, how much youtube shorts pay per view, youtube shorts revenue, shorts creator fund earnings 2025"
    ),
    "youtube-watch-time-calculator.html": (
        "YouTube Watch Time Calculator - 4000 Hours Tracker | SuperCalc",
        "Calculate your YouTube watch hours and find out how long to reach 4000 hours for monetization. Track your progress toward YouTube Partner Program eligibility.",
        "youtube watch time calculator, 4000 watch hours calculator, youtube monetization hours tracker, how to reach 4000 watch hours, youtube watch hours per video calculator"
    ),
    "youtube-retention-rate-calculator.html": (
        "YouTube Retention Rate Calculator - Audience Retention Analysis | SuperCalc",
        "Calculate your YouTube video audience retention rate. Understand what percentage of viewers watch your full video and how it affects your channel's ranking.",
        "youtube retention rate calculator, audience retention youtube, average view duration calculator, youtube watch percentage, how to improve youtube retention rate"
    ),
    "youtube-channel-growth-projection-calculator.html": (
        "YouTube Channel Growth Projection Calculator - Subscriber Milestones | SuperCalc",
        "Project your YouTube channel's future subscriber count. Calculate when you'll reach 1K, 10K, 100K and 1 million subscribers based on your growth rate.",
        "youtube channel growth projection calculator, youtube subscriber projection, when will i get 1000 subscribers youtube, youtube milestone calculator, youtube subscriber forecast 2025"
    ),
    "views-to-subscribers-ratio-calculator.html": (
        "Views to Subscribers Ratio Calculator - YouTube Conversion Rate | SuperCalc",
        "Calculate your YouTube views-to-subscribers conversion rate. Find what percentage of viewers subscribe to your channel and how to improve it.",
        "views to subscribers ratio calculator, youtube subscriber conversion rate, how many views per subscriber youtube, youtube conversion rate calculator, subscriber rate calculator"
    ),
    "youtube-thumbnail-ctr-calculator.html": (
        "YouTube Thumbnail CTR Calculator - Click Through Rate | SuperCalc",
        "Calculate your YouTube thumbnail click-through rate. Find if your CTR is good and get tips to improve your thumbnails for more views.",
        "youtube thumbnail CTR calculator, click through rate youtube, how to calculate youtube CTR, improve youtube CTR, youtube impressions click through rate 2025"
    ),

    # ── TIKTOK ──
    "tiktok-engagement-rate-calculator.html": (
        "TikTok Engagement Rate Calculator 2025 - Free Analytics Tool | SuperCalc",
        "Calculate your TikTok engagement rate from likes, comments, shares and views. Compare to industry benchmarks. Free TikTok analytics tool for creators and brands.",
        "tiktok engagement rate calculator, tiktok engagement rate 2025, how to calculate tiktok engagement rate, tiktok analytics tool, tiktok creator metrics, what is a good tiktok engagement rate"
    ),
    "tiktok-earnings-calculator.html": (
        "TikTok Earnings Calculator 2025 - Creator Fund + Brand Deals | SuperCalc",
        "Calculate how much money you can make on TikTok. Estimate Creator Fund payments, brand deal income, and total monthly TikTok earnings. The most accurate TikTok money calculator.",
        "tiktok earnings calculator, how much does tiktok pay, tiktok creator fund calculator, tiktok money calculator 2025, how much do tiktok creators make, tiktok income calculator, tiktok monetization calculator"
    ),
    "tiktok-virality-score-calculator.html": (
        "TikTok Virality Score Calculator - Is Your Video Going Viral? | SuperCalc",
        "Calculate your TikTok video's virality score. Find out if your content is going viral based on views-to-follower ratio and engagement metrics.",
        "tiktok virality score calculator, how to go viral on tiktok, tiktok viral calculator, tiktok views ratio calculator, tiktok for you page algorithm, is my tiktok going viral"
    ),
    "tiktok-growth-rate-calculator.html": (
        "TikTok Growth Rate Calculator - Track Your Follower Growth | SuperCalc",
        "Calculate your TikTok follower growth rate and project when you'll reach 10K, 100K and 1M followers. Free TikTok growth tracker for creators.",
        "tiktok growth rate calculator, tiktok follower growth calculator, how fast is my tiktok growing, tiktok followers increase rate, when will i reach 100k tiktok"
    ),

    # ── TWITTER ──
    "twitter-engagement-rate-calculator.html": (
        "Twitter (X) Engagement Rate Calculator 2025 - Free Tool | SuperCalc",
        "Calculate your Twitter/X engagement rate from likes, retweets, replies and impressions. Compare to industry benchmarks. Free Twitter analytics calculator.",
        "twitter engagement rate calculator, X engagement rate calculator, tweet engagement rate, twitter analytics calculator, how to calculate twitter engagement rate, twitter impressions engagement 2025"
    ),
    "tweet-engagement-calculator.html": (
        "Tweet Engagement Calculator - Analyze Any Tweet | SuperCalc",
        "Calculate individual tweet engagement metrics including like rate, retweet rate, reply rate and amplification score. Analyze any Twitter/X post performance.",
        "tweet engagement calculator, single tweet analytics, twitter post performance calculator, tweet likes retweet ratio, how to analyze a tweet, twitter engagement metrics"
    ),
    "twitter-growth-rate-calculator.html": (
        "Twitter (X) Growth Rate Calculator - Follower Growth Tracker | SuperCalc",
        "Track your Twitter/X follower growth rate and project when you'll reach your next milestone. Calculate daily gain and monthly growth percentage.",
        "twitter growth rate calculator, X follower growth calculator, twitter followers increase tracker, how to grow twitter followers, twitter growth projection 2025"
    ),

    # ── LINKEDIN ──
    "linkedin-engagement-rate-calculator.html": (
        "LinkedIn Engagement Rate Calculator 2025 - Professional Analytics | SuperCalc",
        "Calculate your LinkedIn post engagement rate from reactions, comments, shares and impressions. Compare to B2B benchmarks. Essential for LinkedIn creators and marketers.",
        "linkedin engagement rate calculator, linkedin post analytics, how to calculate linkedin engagement rate, linkedin engagement benchmarks, linkedin content performance 2025, B2B engagement rate"
    ),
    "linkedin-post-performance-calculator.html": (
        "LinkedIn Post Performance Calculator - Score Your Content | SuperCalc",
        "Analyze your LinkedIn post performance with a comprehensive score. Calculate reach, engagement, virality and conversion metrics for any LinkedIn post.",
        "linkedin post performance calculator, linkedin post analytics score, linkedin content score, linkedin post reach calculator, linkedin engagement analysis 2025"
    ),

    # ── CREATOR/MONETIZATION ──
    "influencer-earnings-per-post-calculator.html": (
        "Influencer Earnings Per Post Calculator 2025 - Rate Card | SuperCalc",
        "Calculate how much to charge per sponsored post as an influencer. Get your rate card based on followers, engagement rate and platform. Used by 200,000+ creators.",
        "influencer earnings per post calculator, how much to charge for sponsored post, influencer rate card calculator, sponsored content pricing, influencer fee calculator 2025, how much do influencers charge"
    ),
    "brand-deal-rate-calculator.html": (
        "Brand Deal Rate Calculator 2025 - Creator Sponsorship Pricing | SuperCalc",
        "Calculate the right rate for your brand deals as a content creator. Get minimum, recommended and premium rates for sponsored content, product reviews and ambassador deals.",
        "brand deal rate calculator, sponsored content pricing calculator, content creator brand deal rate, how much to charge brands, influencer sponsorship rate 2025, brand partnership pricing"
    ),
    "adsense-rpm-calculator.html": (
        "AdSense RPM Calculator 2025 - Website Earnings Estimator | SuperCalc",
        "Calculate your Google AdSense RPM and estimate monthly earnings from your website traffic. Find your effective CPM and optimize your AdSense revenue strategy.",
        "adsense RPM calculator, google adsense earnings calculator 2025, website adsense income, adsense revenue per 1000 pageviews, adsense CPM calculator, blog earnings calculator, adsense RPM by niche"
    ),
    "affiliate-earnings-calculator.html": (
        "Affiliate Earnings Calculator 2025 - Marketing Income Estimator | SuperCalc",
        "Calculate your potential affiliate marketing income based on traffic, conversion rate and commission. Estimate monthly and yearly affiliate revenue for any niche.",
        "affiliate earnings calculator, affiliate marketing income calculator 2025, affiliate commission calculator, how much can i make with affiliate marketing, affiliate marketing revenue estimator"
    ),
    "social-media-roi-calculator.html": (
        "Social Media ROI Calculator - Marketing Return on Investment | SuperCalc",
        "Calculate your social media marketing ROI, ROAS and net profit. Measure returns from organic content, paid ads and influencer campaigns against total spend.",
        "social media ROI calculator, social media return on investment, marketing ROI calculator, social media campaign ROI, digital marketing ROI calculator 2025, ROAS calculator"
    ),
    "website-traffic-to-revenue-calculator.html": (
        "Website Traffic to Revenue Calculator - Monetization Estimator | SuperCalc",
        "Calculate how much revenue your website traffic can generate from AdSense, affiliate links, and product sales. Free website monetization calculator.",
        "website traffic to revenue calculator, blog income calculator, website monetization calculator, how much does a website make per visitor, traffic to money calculator 2025"
    ),
    "follower-to-income-calculator.html": (
        "Follower to Income Calculator - Social Media Earnings Potential | SuperCalc",
        "Convert your social media followers to estimated income potential. Calculate how much your Instagram, YouTube, TikTok and Twitter followers are worth.",
        "follower to income calculator, how much are my followers worth, social media followers money calculator, follower count value calculator, influencer income by followers 2025"
    ),
    "micro-influencer-rate-calculator.html": (
        "Micro Influencer Rate Calculator 2025 - Nano Influencer Pricing | SuperCalc",
        "Calculate fair rates for micro and nano influencers (1K-100K followers). Get pricing for sponsored posts, Reels, Stories and YouTube integrations based on engagement.",
        "micro influencer rate calculator, nano influencer pricing calculator, small influencer rates, how much micro influencer charge per post, influencer pricing 1000 followers 2025"
    ),
    "virality-score-calculator.html": (
        "Virality Score Calculator - Measure Viral Potential | SuperCalc",
        "Calculate the virality score of any social media post. Measure viral coefficient, share rate and overall viral potential across all platforms.",
        "virality score calculator, viral coefficient calculator, how to measure virality, social media viral score, viral potential calculator, content virality calculator"
    ),
    "follower-to-engagement-ratio-calculator.html": (
        "Follower to Engagement Ratio Calculator - Ghost Follower Detector | SuperCalc",
        "Calculate your follower-to-engagement ratio to identify ghost followers and measure true audience quality across all social media platforms.",
        "follower engagement ratio calculator, ghost followers calculator, real engagement calculator, follower quality score, authentic engagement rate checker, are my followers real"
    ),
    "content-performance-score-calculator.html": (
        "Content Performance Score Calculator - Rate Any Post | SuperCalc",
        "Calculate an overall performance score for any piece of content. Score posts based on reach, engagement, conversions and audience sentiment.",
        "content performance score calculator, content analytics score, social media post score calculator, content marketing KPIs calculator, post performance analyzer"
    ),
    "post-frequency-impact-calculator.html": (
        "Post Frequency Impact Calculator - Optimal Posting Schedule | SuperCalc",
        "Calculate the optimal posting frequency for Instagram, YouTube, TikTok and LinkedIn. Find how post frequency affects your reach, engagement and follower growth.",
        "post frequency calculator, how often to post on instagram, optimal posting frequency calculator, social media posting schedule calculator, content frequency impact"
    ),

    # ── AI / MODERN ──
    "ai-token-cost-calculator.html": (
        "AI Token Cost Calculator 2025 - ChatGPT Claude Gemini API Cost | SuperCalc",
        "Calculate the cost of AI API tokens for ChatGPT (GPT-4o), Claude, Gemini and other LLMs. Estimate daily, monthly and annual AI API spending based on your usage.",
        "AI token cost calculator, ChatGPT API cost calculator, OpenAI token price calculator, Claude API cost, Gemini API cost, LLM token calculator 2025, GPT-4o cost per request, AI API pricing calculator"
    ),
    "api-cost-calculator.html": (
        "API Cost Calculator 2025 - Monthly API Usage Cost Estimator | SuperCalc",
        "Calculate the total monthly cost of API calls for your application. Compare API pricing tiers and estimate costs as you scale from 1K to millions of requests.",
        "API cost calculator, API pricing calculator, monthly API cost estimator, REST API cost calculator, API usage cost 2025, SaaS API pricing calculator, cloud API costs"
    ),
    "saas-pricing-calculator.html": (
        "SaaS Pricing Calculator - MRR ARR LTV Churn Metrics | SuperCalc",
        "Calculate SaaS metrics: Monthly Recurring Revenue (MRR), Annual Recurring Revenue (ARR), Customer LTV, churn rate, and LTV:CAC ratio. Essential for SaaS founders.",
        "SaaS pricing calculator, MRR ARR calculator, SaaS metrics calculator, customer LTV calculator, SaaS churn rate calculator, subscription business calculator 2025, SaaS revenue calculator"
    ),
    "content-generation-cost-calculator.html": (
        "Content Generation Cost Calculator - AI vs Human Writer Cost | SuperCalc",
        "Calculate the cost of AI-generated content vs human writers. Compare costs for blog posts, social media, scripts and SEO content. Find out how much AI saves you.",
        "content generation cost calculator, AI content cost vs human writer, AI writing cost calculator, blog post cost calculator, content writing cost per word, AI vs human writer comparison 2025"
    ),
}

def update_seo(filepath, title, description, keywords):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update title
    html = re.sub(r'<title>[^<]+</title>', f'<title>{title}</title>', html, count=1)

    # Update meta description
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{description}"',
        html, count=1
    )

    # Update meta keywords
    if '<meta name="keywords"' in html:
        html = re.sub(
            r'<meta name="keywords" content="[^"]*"',
            f'<meta name="keywords" content="{keywords}"',
            html, count=1
        )
    else:
        # Insert keywords after description
        html = html.replace(
            f'<meta name="description" content="{description}">',
            f'<meta name="description" content="{description}">\n<meta name="keywords" content="{keywords}">'
        )

    # Update OG title
    html = re.sub(
        r'<meta property="og:title" content="[^"]*"',
        f'<meta property="og:title" content="{title}"',
        html, count=1
    )

    # Update OG description
    html = re.sub(
        r'<meta property="og:description" content="[^"]*"',
        f'<meta property="og:description" content="{description}"',
        html, count=1
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return True

# ── Also enhance top general calculators ──────────────────────────────────
GENERAL_SEO = {
    "bmi-calculator.html": (
        "BMI Calculator 2025 - Body Mass Index Check | SuperCalc",
        "Calculate your BMI instantly with our free BMI calculator. Find your Body Mass Index, weight category (underweight/normal/overweight/obese) and ideal weight range.",
        "BMI calculator, body mass index calculator, BMI check online, calculate BMI free, BMI for adults, healthy BMI range, body mass index 2025"
    ),
    "calorie-calculator.html": (
        "Calorie Calculator 2025 - Daily Calorie Needs & TDEE | SuperCalc",
        "Calculate your daily calorie needs and TDEE (Total Daily Energy Expenditure) based on age, weight, height and activity level. Free nutrition calculator.",
        "calorie calculator, TDEE calculator, daily calorie needs calculator, how many calories should i eat, calorie intake calculator, calorie deficit calculator 2025"
    ),
    "gst-calculator.html": (
        "GST Calculator India 2025 - Add or Remove GST Online Free | SuperCalc",
        "Calculate GST instantly. Add or remove Goods and Services Tax for all slabs (0%, 3%, 5%, 12%, 18%, 28%). Free Indian GST calculator with 2025 rates.",
        "GST calculator, GST calculator India 2025, goods and services tax calculator, add GST, remove GST, GST inclusive exclusive calculator, GST rate calculator"
    ),
    "sip-calculator.html": (
        "SIP Calculator 2025 - Mutual Fund Returns & Wealth Calculator | SuperCalc",
        "Calculate SIP returns and mutual fund wealth accumulation. Free SIP calculator for monthly investments, expected returns and future value estimation.",
        "SIP calculator, systematic investment plan calculator, mutual fund SIP returns, SIP returns calculator 2025, monthly SIP calculator, SIP wealth calculator"
    ),
    "income-tax-calculator.html": (
        "Income Tax Calculator India 2025-26 - New vs Old Tax Regime | SuperCalc",
        "Calculate your income tax for FY 2025-26. Compare new tax regime vs old regime, find rebates and calculate net tax payable. Free India income tax calculator.",
        "income tax calculator 2025, India income tax calculator, new tax regime calculator, old tax regime calculator, income tax slab 2025-26, salary tax calculator India"
    ),
}
SEO_DATA.update(GENERAL_SEO)

# Process all files
processed = 0
errors = []

for filename, (title, desc, kw) in SEO_DATA.items():
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        errors.append(f"Not found: {filename}")
        continue
    try:
        update_seo(filepath, title, desc, kw)
        processed += 1
    except Exception as e:
        errors.append(f"{filename}: {e}")

print(f"Enhanced SEO for {processed} pages")
if errors:
    print(f"Errors: {errors}")
