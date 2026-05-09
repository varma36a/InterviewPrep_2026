namespace DesignPatternsLearnignFolder.Patterns.Behavioral;

internal static class CommandPattern
{
    internal static void Run()
    {
        var vmService = new VmService();
        var invoker = new OperationInvoker();
        invoker.Enqueue(new StartVmCommand(vmService, "vm-prod-1"));
        invoker.Enqueue(new StopVmCommand(vmService, "vm-test-3"));
        invoker.RunAll();
    }
}

internal interface ICommand { void Execute(); }
internal sealed class VmService { internal void Start(string vm) => Console.WriteLine($"Command -> Started {vm}"); internal void Stop(string vm) => Console.WriteLine($"Command -> Stopped {vm}"); }
internal sealed class StartVmCommand(VmService service, string vm) : ICommand { public void Execute() => service.Start(vm); }
internal sealed class StopVmCommand(VmService service, string vm) : ICommand { public void Execute() => service.Stop(vm); }
internal sealed class OperationInvoker
{
    private readonly Queue<ICommand> _commands = new();
    internal void Enqueue(ICommand command) => _commands.Enqueue(command);
    internal void RunAll() { while (_commands.TryDequeue(out var cmd)) cmd.Execute(); }
}
