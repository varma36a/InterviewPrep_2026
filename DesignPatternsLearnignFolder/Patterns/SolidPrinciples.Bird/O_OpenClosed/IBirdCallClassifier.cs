namespace SolidPrinciples.Bird.O_OpenClosed;

/// <summary>
/// O — Open/Closed: extend with new classifiers without modifying the orchestrator.
/// </summary>
public interface IBirdCallClassifier
{
    string Species { get; }
    bool CanClassify(string audioSample);
    string Classify(string audioSample);
}
