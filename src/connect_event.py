def get_parameters(event):
    details = event.get("Details",{})
    parameters = details.get("Parameters",{})
    return parameters
