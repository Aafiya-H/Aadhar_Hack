<template>
  <div class="col-12 grid-margin stretch-card">
        <div class="card card-rounded">
            <div class="card-body">
            <div class="d-sm-flex justify-content-between align-items-start">
                <div>
                <h4 class="card-title card-title-dash">Past Requests</h4>
                <p class="card-subtitle card-subtitle-dash">You have 3 past requests</p>
                </div>
            </div>
            <div class="table-responsive  mt-1">
                <table class="table select-table">
                <thead>
                    <tr>
                    <th># Req. ID</th>
                    <th>Landlord</th>
                    <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="request in pastRequests" v-bind:key="request.id">
                        <td>
                            #{{ request.id }}
                        </td>
                        <td>
                            <div>
                                <h6>{{ request.landlord }}</h6>
                            </div>
                        </td>
                        <td><div class="badge badge-opacity-warning">{{  }}</div></td>
                    </tr>
                    <tr>
                        <td>
                            #1317
                        </td>
                        <td>
                            <div>
                                <h6>Sam Washington</h6>
                                <p>Bangalore</p>
                            </div>
                        </td>
                        <td><div class="badge badge-opacity-danger">Rejected</div></td>
                    </tr>
                    <tr>
                        <td>
                            #1174
                        </td>
                        <td>
                            <div>
                                <h6>Joshua Washington</h6>
                                <p>Hydrabad</p>
                            </div>
                        </td>
                        <td><div class="badge badge-opacity-success">Accepted</div></td>
                    </tr>
                </tbody>
                </table>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['pastRequests']
}
</script>

<style>

</style>