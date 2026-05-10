# Twingate Release Stages

## Summary
Twingate releases features in two stages: Beta and General Availability (GA). Beta is for testing with limited support guarantees, while GA indicates production-ready features with full support.

## Key Information

### Beta Stage
- Available for opt-in testing or enabled only for new networks
- May have bugs, limited functionality, or incomplete features
- Documentation provided but may be incomplete
- **No guaranteed support**
- Breaking changes possible
- Not fully optimized for performance

### General Availability (GA) Stage
- Fully released for public and production use
- Available to both new and existing networks
- Full formal support through regular channels
- Breaking changes avoided whenever possible
- Comprehensive documentation with known feature gaps outlined
- Optimized and scalable for production use

## Comparison Table

| Area | Beta | GA |
|------|------|----|
| Functionality | May be incomplete | Feature-complete |
| Reliability | Possible minor issues | Thoroughly tested |
| Stability | Breaking changes possible | Breaking changes avoided |
| Performance | Not fully optimized | Production-optimized |
| Support | Not guaranteed | Full formal support |
| Documentation | May be incomplete | Comprehensive |
| Availability | Opt-in / new networks only | New and existing networks |

## Gotchas
- Beta features may introduce breaking changes — avoid relying on them in production pipelines
- Support requests for Beta features may not be addressed
- Beta availability may be restricted to new networks only, meaning existing networks must opt-in separately if eligible
- GA documentation explicitly notes known feature gaps — review before implementation

## Related Docs
- Individual feature documentation (indicates Beta or GA status per feature)