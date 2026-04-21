# Gamma — Presentation Builder Capability Card

**Platform:** Gamma (gamma.app)  
**Version:** Public API v1.0  
**Current State:** ACTIVE — 10-slide deck created via API  
**Docs:** https://docs.gamma.app

## Authentication
```bash
export GAMMA_API_KEY=your_key_here
```

## What It Does
AI-powered presentation generator. Send structured text, get a designed deck back. Supports AI-generated images, clean layouts, and collaborative editing.

## Key Endpoints

### Create Presentation
```bash
curl -X POST "https://public-api.gamma.app/v1.0/generations" \
  -H "X-API-KEY: $GAMMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "inputText": "Slide 1 title\n--\nSlide 2 title\nContent...",
    "textMode": "generate",
    "format": "presentation",
    "cardSplit": "inputTextBreaks",
    "textOptions": {
      "amount": "detailed",
      "tone": "strategic, confident, pragmatic",
      "audience": "senior partners at a design innovation consulting firm"
    }
  }'
```

### Check Generation Status
```bash
curl -X GET "https://public-api.gamma.app/v1.0/generations/{gen_id}" \
  -H "X-API-KEY: $GAMMA_API_KEY"
```

## IAC Deck Preset
```python
PAYLOAD = {
    "inputText": DECK_TEXT,
    "textMode": "generate",
    "format": "presentation",
    "cardSplit": "inputTextBreaks",
    "textOptions": {
        "amount": "detailed",
        "tone": "strategic, confident, pragmatic",
        "audience": "senior partners at a design innovation consulting firm"
    },
    "imageOptions": {"source": "aiGenerated", "stylePreset": "minimal"},
    "additionalInstructions": (
        "Senior executive audience. Clean modern aesthetic. Dark navy and white with bold stat callouts. "
        "Bullet points and bold headlines only — no paragraphs. "
        "Big number callouts for: 31.6%, 12-18 months, $16M to $50M+. "
        "Minimalist layouts, strong white space."
    )
}
```

## Use Cases for IAC
1. **Pitch decks** — Create new decks for client meetings (Kyle, Co-CEOs)
2. **Package presentations** — Visual walkthrough of Catalyst Sprint, Fabric LITE, etc.
3. **Board-ready materials** — Financial projections, timeline, ROI case
4. **Internal briefings** — Partner group presentations, team alignment

## Known Issues
- **API quota limits** — Monitor `credits` field in response
- **Image generation delays** — AI images add 30–90s to generation time
- **Edit URL required:** Always capture `gamma_id` — edit URL is `https://gamma.app/editor/{gamma_id}`

## Integration Rules
- Always store `gamma_id` and `gen_id` in vault for later editing
- Use `"cardSplit": "inputTextBreaks"` with `--` separators between slides
- Limit to 12 slides max for Kyle attention span
- Test on dummy deck before mission-critical creation
