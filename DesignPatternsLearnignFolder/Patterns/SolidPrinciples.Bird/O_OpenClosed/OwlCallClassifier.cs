namespace SolidPrinciples.Bird.O_OpenClosed;

/// <summary>
/// Added later — no changes required to BirdCallOrchestrator (open for extension, closed for modification).
/// </summary>
public sealed class OwlCallClassifier : IBirdCallClassifier
{
    public string Species => "Owl";

    public bool CanClassify(string audioSample) =>
        audioSample.Contains("hoot", StringComparison.OrdinalIgnoreCase);

    public string Classify(string audioSample) =>
        $"Owl detected — low hoot in '{audioSample}'.";
}
