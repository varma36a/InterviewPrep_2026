namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class MementoPattern
{
    internal static void Run()
    {
        var editor = new DocumentEditor();
        editor.Content = "Draft v1";
        var history = new DraftHistory();
        history.Save(editor.Save());
        editor.Content = "Draft v2 with edits";
        editor.Restore(history.Undo());
        Console.WriteLine($"Memento -> Restored content: {editor.Content}");
    }
}

internal sealed class EditorMemento(string content) { internal string Content { get; } = content; }
internal sealed class DocumentEditor
{
    internal string Content { get; set; } = string.Empty;
    internal EditorMemento Save() => new(Content);
    internal void Restore(EditorMemento snapshot) => Content = snapshot.Content;
}
internal sealed class DraftHistory
{
    private readonly Stack<EditorMemento> _history = new();
    internal void Save(EditorMemento snapshot) => _history.Push(snapshot);
    internal EditorMemento Undo() => _history.Pop();
}
