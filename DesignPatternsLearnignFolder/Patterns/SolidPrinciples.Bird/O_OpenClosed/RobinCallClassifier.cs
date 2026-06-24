namespace SolidPrinciples.Bird.O_OpenClosed;

public sealed class RobinCallClassifier : IBirdCallClassifier
{
    public string Species => "Robin";

    public bool CanClassify(string audioSample) =>
        audioSample.Contains("cheer-up", StringComparison.OrdinalIgnoreCase);

    public string Classify(string audioSample) =>
        $"Robin detected — cheerful whistle pattern in '{audioSample}'.";
}
