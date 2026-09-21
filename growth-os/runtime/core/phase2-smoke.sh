#!/usr/bin/env bash
set -euo pipefail

pass() { printf 'PASS %s\n' "$1"; }
fail() { printf 'FAIL %s\n' "$1" >&2; exit 1; }
retry_http() {
  local url="$1" name="$2"
  for _ in $(seq 1 30); do
    if curl -fsS "$url" >/dev/null 2>&1; then
      pass "$name"
      return 0
    fi
    sleep 2
  done
  fail "$name"
}

systemctl is-active --quiet docker && pass docker-active || fail docker-active

docker inspect -f '{{.State.Running}}' growthos-activepieces-app | grep -qx true && pass activepieces-app || fail activepieces-app
docker inspect -f '{{.State.Running}}' growthos-activepieces-worker | grep -qx true && pass activepieces-worker || fail activepieces-worker
docker inspect -f '{{.State.Running}}' growthos-postgres | grep -qx true && pass postgres-container || fail postgres-container
docker inspect -f '{{.State.Running}}' growthos-redis | grep -qx true && pass redis-container || fail redis-container
docker inspect -f '{{.State.Running}}' growthos-uptime-kuma | grep -qx true && pass uptime-kuma || fail uptime-kuma
docker inspect -f '{{.State.Running}}' growthos-dockge | grep -qx true && pass dockge || fail dockge

retry_http http://localhost:8080/api/v1/health activepieces-health
docker exec growthos-postgres pg_isready -U postgres -d activepieces >/dev/null && pass postgres-ready || fail postgres-ready
test "$(docker exec growthos-redis redis-cli ping)" = "PONG" && pass redis-ping || fail redis-ping
retry_http http://localhost:3001/ kuma-http
retry_http http://localhost:5001/ dockge-http

for p in 8080 3001 5001; do
  ss -ltn "sport = :$p" | grep -q LISTEN || fail "port-$p"
done
pass expected-ports

echo PHASE2_SMOKE_OK
