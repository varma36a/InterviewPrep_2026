namespace SolidPrinciples.Bird.O_OpenClosed;

public sealed class CrowCallClassifier : IBirdCallClassifier
{
    public string Species => "Crow";

    public bool CanClassify(string audioSample) =>
        audioSample.Contains("caw", StringComparison.OrdinalIgnoreCase);

    public string Classify(string audioSample) =>
        $"Crow detected — harsh 'caw' in '{audioSample}'.";
}
