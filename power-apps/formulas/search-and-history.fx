// Sanitized Power Fx excerpts; public data-source names are generic.
With(
    {selectedVehicle: Upper(Trim(txtVehicleSearch.Text))},
    If(
        IsBlank(selectedVehicle),
        Notify("Enter a vehicle identifier.", NotificationType.Information),
        Set(varSelectedVehicle, LookUp(VehicleLocationRegistry, VehicleId = selectedVehicle));
        ClearCollect(
            colVehicleEvents,
            SortByColumns(
                Filter(VehicleEventHistory, VehicleId = selectedVehicle),
                "EventDate",
                SortOrder.Descending
            )
        )
    )
)

