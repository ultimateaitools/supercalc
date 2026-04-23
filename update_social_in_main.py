# -*- coding: utf-8 -*-
import os

BASE = r"d:\Datomate AI Lab\CalcWebsite"

NEW_CALCULATORS = """
  // Social Media - Instagram
  { name: "Instagram Engagement Rate Calculator", url: "instagram-engagement-rate-calculator.html", icon: "&#128247;", cat: "Social", desc: "Calculate your IG engagement rate", badge: "hot" },
  { name: "Instagram Engagement Per Post", url: "instagram-engagement-per-post-calculator.html", icon: "&#128247;", cat: "Social", desc: "Avg engagement per Instagram post" },
  { name: "Instagram Reach Rate Calculator", url: "instagram-reach-rate-calculator.html", icon: "&#128247;", cat: "Social", desc: "What % of followers see your posts" },
  { name: "Instagram Growth Rate Calculator", url: "instagram-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "Track Instagram follower growth", badge: "new" },
  { name: "Instagram Influencer Earnings", url: "instagram-influencer-earnings-calculator.html", icon: "&#128176;", cat: "Social", desc: "Estimate Instagram sponsored post rate", badge: "hot" },
  { name: "Instagram Reels Earnings", url: "instagram-reels-earnings-calculator.html", icon: "&#127909;", cat: "Social", desc: "Reels monetization estimator", badge: "new" },

  // Social Media - YouTube
  { name: "YouTube Engagement Rate Calculator", url: "youtube-engagement-rate-calculator.html", icon: "&#127909;", cat: "Social", desc: "YouTube likes/comments vs views" },
  { name: "YouTube Money Calculator", url: "youtube-money-calculator.html", icon: "&#128176;", cat: "Social", desc: "Estimate YouTube channel earnings", badge: "hot" },
  { name: "YouTube CPM Calculator", url: "youtube-cpm-calculator.html", icon: "&#128200;", cat: "Social", desc: "YouTube cost per mille ad rate", badge: "hot" },
  { name: "YouTube RPM Calculator", url: "youtube-rpm-calculator.html", icon: "&#128200;", cat: "Social", desc: "Revenue per 1000 YouTube views", badge: "hot" },
  { name: "YouTube Growth Rate Calculator", url: "youtube-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "YouTube subscriber growth tracker" },
  { name: "YouTube Shorts Earnings", url: "youtube-shorts-earnings-calculator.html", icon: "&#127909;", cat: "Social", desc: "Shorts monetization estimator", badge: "new" },
  { name: "YouTube Watch Time Calculator", url: "youtube-watch-time-calculator.html", icon: "&#9201;", cat: "Social", desc: "4000 hours monetization tracker" },
  { name: "YouTube Retention Rate Calculator", url: "youtube-retention-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "Audience retention analysis" },
  { name: "YouTube Channel Growth Projection", url: "youtube-channel-growth-projection-calculator.html", icon: "&#128200;", cat: "Social", desc: "Project subscriber milestones" },
  { name: "Views to Subscribers Ratio", url: "views-to-subscribers-ratio-calculator.html", icon: "&#127909;", cat: "Social", desc: "YouTube subscriber conversion rate" },
  { name: "YouTube Thumbnail CTR Calculator", url: "youtube-thumbnail-ctr-calculator.html", icon: "&#128249;", cat: "Social", desc: "Click-through rate for thumbnails" },

  // Social Media - TikTok
  { name: "TikTok Engagement Rate Calculator", url: "tiktok-engagement-rate-calculator.html", icon: "&#127925;", cat: "Social", desc: "TikTok likes/comments/shares rate", badge: "hot" },
  { name: "TikTok Earnings Calculator", url: "tiktok-earnings-calculator.html", icon: "&#128176;", cat: "Social", desc: "TikTok creator fund income", badge: "hot" },
  { name: "TikTok Virality Score Calculator", url: "tiktok-virality-score-calculator.html", icon: "&#128293;", cat: "Social", desc: "Is your TikTok going viral?" },
  { name: "TikTok Growth Rate Calculator", url: "tiktok-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "TikTok follower growth tracker" },

  // Social Media - Twitter & LinkedIn
  { name: "Twitter (X) Engagement Rate", url: "twitter-engagement-rate-calculator.html", icon: "&#128038;", cat: "Social", desc: "Tweet engagement rate calculator" },
  { name: "Tweet Engagement Calculator", url: "tweet-engagement-calculator.html", icon: "&#128038;", cat: "Social", desc: "Single tweet metrics analyzer" },
  { name: "Twitter Growth Rate Calculator", url: "twitter-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "Twitter follower growth tracker" },
  { name: "LinkedIn Engagement Rate", url: "linkedin-engagement-rate-calculator.html", icon: "&#128188;", cat: "Social", desc: "LinkedIn post engagement rate", badge: "hot" },
  { name: "LinkedIn Post Performance", url: "linkedin-post-performance-calculator.html", icon: "&#128202;", cat: "Social", desc: "LinkedIn content performance score" },

  // Creator Economy / Monetization
  { name: "Influencer Earnings Per Post", url: "influencer-earnings-per-post-calculator.html", icon: "&#128176;", cat: "Social", desc: "Sponsored post rate calculator", badge: "hot" },
  { name: "Brand Deal Rate Calculator", url: "brand-deal-rate-calculator.html", icon: "&#129534;", cat: "Social", desc: "Content creator brand deal pricing", badge: "new" },
  { name: "AdSense RPM Calculator", url: "adsense-rpm-calculator.html", icon: "&#128176;", cat: "Social", desc: "Google AdSense earnings estimator", badge: "hot" },
  { name: "Affiliate Earnings Calculator", url: "affiliate-earnings-calculator.html", icon: "&#128200;", cat: "Social", desc: "Affiliate marketing income estimator" },
  { name: "Social Media ROI Calculator", url: "social-media-roi-calculator.html", icon: "&#128200;", cat: "Social", desc: "Marketing ROI and ROAS calculator" },
  { name: "Website Traffic to Revenue", url: "website-traffic-to-revenue-calculator.html", icon: "&#128200;", cat: "Social", desc: "Website monetization estimator" },
  { name: "Follower to Income Calculator", url: "follower-to-income-calculator.html", icon: "&#128176;", cat: "Social", desc: "What your followers are worth" },
  { name: "Micro Influencer Rate Calculator", url: "micro-influencer-rate-calculator.html", icon: "&#128247;", cat: "Social", desc: "Nano and micro influencer pricing" },
  { name: "Virality Score Calculator", url: "virality-score-calculator.html", icon: "&#128293;", cat: "Social", desc: "Social media viral coefficient" },
  { name: "Follower to Engagement Ratio", url: "follower-to-engagement-ratio-calculator.html", icon: "&#128290;", cat: "Social", desc: "Ghost follower detector" },
  { name: "Content Performance Score", url: "content-performance-score-calculator.html", icon: "&#128202;", cat: "Social", desc: "Overall content effectiveness score" },
  { name: "Post Frequency Impact Calculator", url: "post-frequency-impact-calculator.html", icon: "&#128197;", cat: "Social", desc: "Optimal posting frequency finder" },

  // AI & Modern Tools
  { name: "AI Token Cost Calculator", url: "ai-token-cost-calculator.html", icon: "&#129302;", cat: "AI Tools", desc: "ChatGPT, Claude, Gemini API costs", badge: "hot" },
  { name: "API Cost Calculator", url: "api-cost-calculator.html", icon: "&#128187;", cat: "AI Tools", desc: "Monthly API usage cost estimator", badge: "new" },
  { name: "SaaS Pricing Calculator", url: "saas-pricing-calculator.html", icon: "&#128200;", cat: "AI Tools", desc: "MRR, ARR, LTV and churn metrics", badge: "hot" },
  { name: "Content Generation Cost", url: "content-generation-cost-calculator.html", icon: "&#128221;", cat: "AI Tools", desc: "AI vs human writer cost comparison", badge: "new" },"""

# Read main.js
main_js_path = os.path.join(BASE, "js", "main.js")
with open(main_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the closing ]; of ALL_CALCULATORS
end_idx = content.index('];')
# Insert new calculators before the closing ];
new_content = content[:end_idx] + NEW_CALCULATORS + '\n' + content[end_idx:]

with open(main_js_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated main.js - added 42 new social/AI calculators")
print(f"New file size: {len(new_content)} chars")
