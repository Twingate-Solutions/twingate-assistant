# Twingate Release Stages

## Summary
Twingate releases features in two stages: Beta and General Availability (GA). Beta is for testing with limited support guarantees, while GA indicates production-ready features with full support.

## Key Information

### Beta Stage
- Available for opt-in testing or enabled only for new networks
- May have bugs, limited functionality, or incomplete documentation
- **No guaranteed support**
- Breaking changes possible
- Not fully optimized or feature-complete

### General Availability (GA) Stage
- Fully released for public and production use
- Available to both new and existing networks
- Full formal support through standard channels
- Breaking changes avoided whenever possible
- Comprehensive documentation provided; known feature gaps documented

## Comparison Table

| Area | Beta | GA |
|------|------|-----|
| Functionality | May be incomplete | Feature-complete, polished UI/UX |
| Reliability | Possible minor issues | Performs as expected |
| Stability | Breaking changes possible | Breaking changes avoided |
| Performance | Not optimized | Optimized for production |
| Support | Not guaranteed | Full formal support |
| Documentation | May be incomplete | Comprehensive |
| Testing | Limited environments | Various real-world environments |
| Availability | Opt-in / new networks only | New and existing networks |

## Gotchas
- Beta features may have **breaking changes** — avoid building critical production workflows on Beta features
- Support requests for Beta features may go unanswered
- Beta availability is limited: may require opt-in or only be accessible to newly created networks
- GA documentation explicitly notes known feature gaps — check these before implementation

## Implementation Guidance
- Use Beta features for evaluation and non-critical testing only
- Before relying on a feature in production, confirm it has reached GA status
- Monitor release notes for Beta-to-GA transitions that may include breaking changes from the Beta version