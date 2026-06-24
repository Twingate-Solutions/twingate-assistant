# Twingate Release Stages

## Summary
Twingate releases features in two stages: Beta and General Availability (GA). Beta is for testing with limited support guarantees, while GA indicates production-ready features with full support. This applies to all publicly released Twingate features.

## Key Information

- **Two stages only**: Beta → General Availability (GA)
- Beta features may have bugs, incomplete functionality, or breaking changes
- GA features are feature-complete, optimized, and fully supported
- Beta availability is opt-in or limited to new networks; GA is available to all networks

## Stage Comparison

| Area | Beta | GA |
|------|------|----|
| Functionality | May be incomplete | Feature-complete, polished UI/UX |
| Reliability | Possible minor issues | Thoroughly tested |
| Stability | May have breaking changes | Breaking changes avoided |
| Performance | Not fully optimized | Optimized and scalable |
| Support | Not guaranteed | Full formal support |
| Documentation | May be incomplete | Comprehensive |
| Testing | Limited environments | Various real-world environments |
| Availability | Opt-in / new networks only | New and existing networks |

## Gotchas

- **No support guarantee in Beta** — do not rely on Beta features for production workloads without accepting that support may be unavailable
- **Breaking changes can occur in Beta** — avoid hard dependencies on Beta APIs or configurations that could break on updates
- **Beta may be restricted** — some Beta features are only enabled for new networks, not existing ones
- **GA documentation notes known gaps** — even GA features may have documented limitations; check release notes

## Related Docs
- Individual feature documentation pages indicate the release stage of each feature