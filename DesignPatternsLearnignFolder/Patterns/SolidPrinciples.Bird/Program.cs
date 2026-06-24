using SolidPrinciples.Bird.D_DependencyInversion;
using SolidPrinciples.Bird.I_InterfaceSegregation;
using SolidPrinciples.Bird.L_LiskovSubstitution;
using SolidPrinciples.Bird.O_OpenClosed;
using SolidPrinciples.Bird.S_SingleResponsibility;

Console.WriteLine("=== SOLID Principles — Bird Use Case ===\n");

WriteSection('S', "Single Responsibility");
SingleResponsibilityDemo.Run();

WriteSection('O', "Open/Closed");
OpenClosedDemo.Run();

WriteSection('L', "Liskov Substitution");
LiskovSubstitutionDemo.Run();

WriteSection('I', "Interface Segregation");
InterfaceSegregationDemo.Run();

WriteSection('D', "Dependency Inversion");
await DependencyInversionDemo.RunAsync();

Console.WriteLine("\n=== Done ===");

static void WriteSection(char principle, string title)
{
    Console.WriteLine($"--- {principle} — {title} ---");
}
