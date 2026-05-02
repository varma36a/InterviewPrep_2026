using TaxCompliancePlatform.Domain.Common;

namespace TaxCompliancePlatform.Domain.Entities;

public sealed class TaxDocument : BaseEntity
{
    public Guid TenantId { get; private set; }
    public Guid UploadedByUserId { get; private set; }
    public string FileName { get; private set; } = string.Empty;
    public string StoragePath { get; private set; } = string.Empty;
    public string ContentType { get; private set; } = string.Empty;
    public long FileSizeInBytes { get; private set; }

    private TaxDocument()
    {
    }

    public TaxDocument(Guid tenantId, Guid uploadedByUserId, string fileName, string storagePath, string contentType, long fileSizeInBytes)
    {
        TenantId = tenantId;
        UploadedByUserId = uploadedByUserId;
        FileName = fileName;
        StoragePath = storagePath;
        ContentType = contentType;
        FileSizeInBytes = fileSizeInBytes;
    }
}
