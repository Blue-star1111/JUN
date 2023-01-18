// grafana base url
export const PARENT_CONNECTED_EVENT = 'parent-connected';
export const grafanaURL = "http://localhost:3000/d-solo/kALdF_h4z/new-dashboard-1?orgId=1&theme=light";

export function fetchUnixTimestamp(param){
    let from = new Date(param + " 00:00:00");
    let to = new Date(param + " 00:00:00");

    to.setDate(to.getDate() + 1);

    return [Math.floor(from.getTime() / 1000) + "000", Math.floor(to.getTime() / 1000)  + "000"];
}