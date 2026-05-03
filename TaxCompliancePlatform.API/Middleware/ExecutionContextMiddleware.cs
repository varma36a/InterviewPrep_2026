using Microsoft.Extensions.Primitives;
using TaxCompliancePlatform.API.Execution;
using TaxCompliancePlatform.Domain.Enums;

namespace TaxCompliancePlatform.API.Middleware;

/// <summary>
/// Builds Domino's scenario metadata for the current HTTP request so HttpRequestExecutionContext can expose it to handlers and services.
/// Runs after tenant resolution so IRequestExecutionContext can combine tenant + franchise headers + correlation.
/// </summary>
public sealed class ExecutionContextMiddleware(RequestDelegate next, IConfiguration configuration)
{
    public const string StoreHeaderName = "X-Domino-Store-Code";
    public const string MarketHeaderName = "X-Domino-Market";
    public const string ChannelHeaderName = "X-Domino-Channel";

    public async Task Invoke(HttpContext context)
    {
        var store = FirstHeaderOrDefault(context.Request.Headers, StoreHeaderName)
            ?? configuration["DominoScenario:DefaultStoreCode"]
            ?? "US-DEMO-0001";

        var market = FirstHeaderOrDefault(context.Request.Headers, MarketHeaderName)
            ?? configuration["DominoScenario:DefaultMarketRegion"]
            ?? "US-IL-CHICAGO";

        var channelRaw = FirstHeaderOrDefault(context.Request.Headers, ChannelHeaderName)
            ?? configuration["DominoScenario:DefaultChannel"]
            ?? "Carryout";

        var channel = ParseChannel(channelRaw);

        context.Items[ExecutionContextHttpKeys.DominoStoreCode] = store.Trim();
        context.Items[ExecutionContextHttpKeys.DominoMarketRegion] = market.Trim();
        context.Items[ExecutionContextHttpKeys.DominoFulfillmentChannel] = channel;

        await next(context);
    }

    private static string? FirstHeaderOrDefault(IHeaderDictionary headers, string name) =>
        headers.TryGetValue(name, out StringValues value) && !string.IsNullOrWhiteSpace(value)
            ? value.ToString()
            : null;

    private static DominoFulfillmentChannel ParseChannel(string raw)
    {
        if (raw.Trim().Equals("Delivery", StringComparison.OrdinalIgnoreCase))
        {
            return DominoFulfillmentChannel.Delivery;
        }

        return DominoFulfillmentChannel.Carryout;
    }
}
