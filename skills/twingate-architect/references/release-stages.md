# Twingate Release Stages

## Summary
Twingate releases features in two stages: Beta and General Availability (GA). Beta is for testing with limited support guarantees, while GA indicates production-ready features with full support.

## Key Information

### Beta Stage
- Available for opt-in testing or enabled only for new networks
- May have bugs, limited functionality, or incomplete features
- Breaking changes possible
- Support **not guaranteed**
- Documentation may be incomplete
- Not fully optimized for performance

### General Availability (GA) Stage
- Fully released for production use
- Feature-complete with polished UI/UX
- Breaking changes avoided whenever possible
- **Full formal support** through regular channels
- Comprehensive documentation provided
- Available to both new and existing networks
- Optimized and scalable for production

## Comparison Table

| Area | Beta | GA |
|------|------|----|
| Functionality | May be incomplete | Feature-complete |
| Reliability | Possible minor issues | Thoroughly tested |
| Stability | May have breaking changes | Breaking changes avoided |
| Performance | Not fully optimized | Optimized/scalable |
| Support | Not guaranteed | Full formal support |
| Documentation | May be incomplete | Comprehensive |
| Testing | Limited environments | Various real-world environments |
| Availability | Opt-in or new networks only | New and existing networks |

## Gotchas
- Beta features may introduce **breaking changes** — avoid relying on them in production pipelines
- Support is explicitly not guaranteed during Beta; do not expect SLA coverage
- Beta availability may be restricted to new networks only, meaning existing networks may not have access to opt in
- GA documentation notes **known feature gaps** — review before implementing

## Actionable Guidance
- Use Beta features for evaluation and non-critical testing only
- For production deployments, confirm a feature has reached GA status before depending on it
- Monitor release notes for Beta features that may introduce breaking changes between versions