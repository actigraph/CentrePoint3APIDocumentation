# Raw Data File Formats

* GT3X - ActiGraph proprietary file format
* CSV - Comma Separated Values
* AVRO - [AVRO](https://avro.apache.org/) file format

-----

## GT3X

See [GT3X File Format](https://github.com/actigraph/GT3X-File-Format) for more details.

-----

## CSV

Standard comma separated values format.

**Header:**

* Serial Number - Activity monitor serial number
* Start Date - Start date of activity in file
* Sample Rate - Sample rate of activity monitor

**Columns:**

|Column|Description|
|------|-----------|
|**Timestamp UTC**|Timestamp of raw data activity record in UTC|
|**Accelerometer X**|Acceleration measured on X axis|
|**Accelerometer Y**|Acceleration measured on Y axis|
|**Accelerometer Z**|Acceleration measured on Z axis|

-----

## AVRO

The CentrePoint API supports export of raw data in the [AVRO](https://avro.apache.org/) format.

The AVRO schema is made up of activity records which have a timestamp (recorded in [UNIX epoch seconds](https://en.wikipedia.org/wiki/Unix_time)) and an array of samples. Each sample record has a X, Y, and Z accelerometer value recorded as a double.

Below is a C# representation of the models recorded in the AVRO format.

```csharp
[DataContract(Name = "Samples", Namespace = "AvroActivity")]
public class AvroSample
{
    public AvroSample() { }
    public AvroSample(double x, double y, double z)
    {
        X = x;
        Y = y;
        Z = z;
    }
    [DataMember(Name = "x")]
    public double X { get; set; }
    [DataMember(Name = "y")]
    public double Y { get; set; }
    [DataMember(Name = "z")]
    public double Z { get; set; }
    public override string ToString()
    {
        return $"X:{X}, Y:{Y}, Z:{Z}";
    }
}
```

```csharp
[DataContract(Name = "Activity", Namespace = "AvroActivity")]
public class AvroActivityRecord
{
    [DataMember(Name = "timestamp")]
    public long Timestamp { get; set; }
    [DataMember(Name = "samples")]
    public AvroSample[] Samples { get; set; }
}
```

