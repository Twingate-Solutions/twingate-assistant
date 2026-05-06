# Twingate Release Stages

## Summary
Twingate releases features through two stages: Beta and General Availability (GA). Beta is for testing with limited support guarantees, while GA indicates production-ready features with full support.

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
- Available to both new and existing networks
- Breaking changes avoided whenever possible
- **Full formal support** through regular channels
- Comprehensive documentation provided
- Optimized and scalable for production

## Comparison Table

| Area | Beta | GA |
|------|------|----|
| Functionality | May be incomplete | Feature-complete, polished UI/UX |
| Reliability | Minor issues possible | Performs as expected |
| Stability | Breaking changes possible | Breaking changes avoided |
| Performance | Not fully optimized | Production-optimized |
| Support | Not guaranteed | Full formal support |
| Documentation | May be incomplete | Comprehensive |
| Testing | Limited environments | Real-world environments |
| Availability | Opt-in / new networks only | New and existing networks |

## Gotchas
- **No support SLA during Beta** — do not rely on Beta features for production workloads without accepting risk
- **Breaking changes can occur in Beta** — integrations or configurations built around Beta features may require updates
- Beta features may be opt-in only and not available to existing networks
- GA documentation explicitly notes known feature gaps — review before implementing

## Related Docs
- Individual feature documentation will indicate current release stage (Beta or GA)