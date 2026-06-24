namespace SolidPrinciples.Bird.O_OpenClosed;

public sealed class BirdCallOrchestrator(IEnumerable<IBirdCallClassifier> classifiers)
{
    public string Identify(string audioSample)
    {
        var match = classifiers.FirstOrDefault(c => c.CanClassify(audioSample));
        return match?.Classify(audioSample)
            ?? $"Unknown bird call: '{audioSample}'.";
    }
}
