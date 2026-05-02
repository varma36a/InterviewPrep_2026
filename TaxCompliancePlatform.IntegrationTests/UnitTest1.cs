using Microsoft.AspNetCore.Mvc.Testing;

namespace TaxCompliancePlatform.IntegrationTests;

public class HealthEndpointTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public HealthEndpointTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task Health_Endpoint_Should_Return_Success()
    {
        var response = await _client.GetAsync("/health");
        response.IsSuccessStatusCode.Should().BeTrue();
    }
}