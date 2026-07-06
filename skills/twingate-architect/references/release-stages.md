# Twingate Release Stages

## Summary
Twingate releases features in two stages: Beta and General Availability (GA). Beta is for testing with limited support guarantees, while GA indicates production-ready features with full support.

## Key Information

- **Two stages only**: Beta → General Availability (GA)
- Beta features may have bugs, incomplete functionality, and breaking changes
- GA features are production-ready, fully tested, and supported through standard channels
- Beta may be opt-in or limited to new networks only; GA is available to all networks

## Stage Comparison

| Area | Beta | GA |
|------|------|----|
| Functionality | May be incomplete | Feature-complete, polished UI/UX |
| Reliability | Minor issues possible | Thoroughly tested |
| Stability | Breaking changes possible | Breaking changes avoided |
| Performance | Not fully optimized | Optimized for production |
| Support | Not guaranteed | Full formal support |
| Documentation | May be incomplete | Comprehensive |
| Testing | Limited environments | Various real-world environments |
| Availability | Opt-in or new networks only | New and existing networks |

## Gotchas

- **No support SLA in Beta**: Do not rely on Beta features for production workloads if support is required
- **Breaking changes in Beta**: Integrations or configurations built on Beta features may break without notice
- **Network availability gap**: Beta features may not be enabled for existing networks — check if your network qualifies before planning adoption
- **Documentation may lag**: Beta docs can be incomplete; GA docs outline known feature gaps explicitly

## Implementation Guidance

- Treat Beta features as experimental; avoid hard dependencies in production pipelines
- When evaluating a feature, check its release stage in the documentation header before implementation
- GA features may still have documented known gaps — review the GA documentation for limitations before deploying

## Related Docs
- Individual feature documentation pages indicate release stage status