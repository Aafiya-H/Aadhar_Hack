<template>
  <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Request New Address</h4>
                  <p class="card-description">
                    Fill out the form to request address from your landlord.
                  </p>
                  <form class="forms-sample">
                    <div class="form-group row">
                      <label>Landlord Aadhar Number</label>
                      <div class="input-group col-xs-12">
                        <input type="text" class="form-control" id="exampleInputUsername2" placeholder="1234-5678-1234">
                      </div>
                    </div>
                    <div class="form-group">
                      <label>Attach Relevant Documents</label>
                      <input type="file" class="file-upload-default">
                      <div class="input-group col-xs-12">
                        <input type="text" class="form-control file-upload-info" disabled="" placeholder="Upload Image">
                        <br>
                      </div>
                      <br>
                      <button class="file-upload-browse btn btn-outline-primary" type="button">Select Documents</button>
                    </div>
                    <div class="form-group row">
                      <label>Additional Note (Will only be seen by your landlord</label>
                      <div class="input-group col-xs-12">
                        <input type="text" class="form-control" id="exampleInputMobile" placeholder="Note">
                      </div>
                    </div>
                    <button type="submit" class="btn btn-primary me-2">Submit</button>
                  </form>
                </div>
              </div>
</template>

<script>
export default {

}
</script>

<style>

</style>