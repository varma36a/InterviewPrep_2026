namespace TaxCompliancePlatform.Application.Common;

/// <summary>
/// Wraps a MediatR command/query with the correlation identifier carried from the transport layer.
/// Application services validate this against ambient context before dispatching to handlers.
/// </summary>
public sealed record ApplicationServiceRequest<TCommand>(string CorrelationId, TCommand Command)
    where TCommand : notnull;
