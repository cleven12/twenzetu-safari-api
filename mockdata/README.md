# TZ Tourism — Mock Data

Ready-to-use JSON mock data and TypeScript types that mirror the exact shape
of every `/api/v1/` endpoint. Drop the `mockdata/` folder into your Next.js
project and start building UI without needing the backend running.

---

## File reference

| File | Mirrors API endpoint | Use for |
|------|----------------------|---------|
| `attractions.json` | `GET /api/v1/attractions/` | Attraction card grids, lists |
| `attraction-detail.json` | `GET /api/v1/attractions/:slug/` | Detail page, image gallery, tips |
| `featured-attractions.json` | `GET /api/v1/attractions/featured/` | Hero carousel, homepage highlights |
| `regions.json` | `GET /api/v1/regions/` | Region filter, region cards |
| `weather.json` | `GET /api/v1/weather/current/`, `forecast/`, `seasonal/` | Weather widget |
| `auth.json` | `POST /api/v1/auth/login/`, `register/`, `GET profile/` | Auth forms |
| `types.ts` | All serializers | TypeScript interfaces for every shape |
| `index.ts` | — | Barrel export for clean imports |

---

## Quick start

### 1 — Copy into your Next.js project

```
your-nextjs-app/
  src/
    mockdata/          ← paste here
      index.ts
      types.ts
      attractions.json
      attraction-detail.json
      featured-attractions.json
      regions.json
      weather.json
      auth.json
```

### 2 — Add `resolveJsonModule` to tsconfig (usually already on)

```json
// tsconfig.json
{
  "compilerOptions": {
    "resolveJsonModule": true
  }
}
```

---

## Usage examples

### Attraction card list

```tsx
// app/attractions/page.tsx
import { attractions } from '@/mockdata';
import type { AttractionListItem } from '@/mockdata';

export default function AttractionsPage() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {(attractions as AttractionListItem[]).map((a) => (
        <AttractionCard key={a.slug} attraction={a} />
      ))}
    </div>
  );
}
```

### Attraction card component

```tsx
// components/AttractionCard.tsx
import Image from 'next/image';
import Link from 'next/link';
import type { AttractionListItem } from '@/mockdata';

const DIFFICULTY_STYLES: Record<string, string> = {
  easy:        'bg-emerald-100 text-emerald-800',
  moderate:    'bg-yellow-100 text-yellow-800',
  challenging: 'bg-orange-100 text-orange-800',
  difficult:   'bg-red-100 text-red-800',
  extreme:     'bg-purple-100 text-purple-800',
};

const CATEGORY_EMOJI: Record<string, string> = {
  mountain: '⛰️', beach: '🏖️', wildlife: '🦁', cultural: '🏛️',
  historical: '🏰', adventure: '🧗', national_park: '🌿',
  island: '🏝️', waterfall: '💧', lake: '🌊', other: '✨',
};

export function AttractionCard({ attraction: a }: { attraction: AttractionListItem }) {
  return (
    <Link href={`/attractions/${a.slug}`}
      className="group bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow overflow-hidden border border-gray-100">
      {/* Image */}
      <div className="relative h-48 bg-green-800">
        {a.featured_image ? (
          <Image src={a.featured_image} alt={a.name} fill className="object-cover" />
        ) : (
          <span className="absolute inset-0 flex items-center justify-center text-6xl">
            {CATEGORY_EMOJI[a.category] ?? '✨'}
          </span>
        )}
        {a.is_featured && (
          <span className="absolute top-3 right-3 bg-amber-400 text-amber-900 text-xs font-bold px-2 py-1 rounded-full">
            ⭐ Featured
          </span>
        )}
        <span className={`absolute bottom-3 left-3 text-xs font-semibold px-2 py-1 rounded-full ${DIFFICULTY_STYLES[a.difficulty_level]}`}>
          {a.difficulty_display}
        </span>
      </div>
      {/* Body */}
      <div className="p-4">
        <h3 className="font-bold text-gray-900 group-hover:text-green-700 transition-colors">
          {a.name}
        </h3>
        <p className="text-xs text-green-700 font-medium mt-1">
          📍 {a.region_name} · {a.category_display}
        </p>
        <p className="text-sm text-gray-500 mt-2 line-clamp-2">
          {a.short_description}
        </p>
        <p className="text-xs text-gray-400 mt-3">
          🗓 {a.best_time_to_visit}
        </p>
      </div>
    </Link>
  );
}
```

### Region card component

```tsx
// components/RegionCard.tsx
import Image from 'next/image';
import type { Region } from '@/mockdata';

export function RegionCard({ region: r }: { region: Region }) {
  return (
    <div className="relative rounded-2xl overflow-hidden h-56 cursor-pointer group">
      {r.image && (
        <Image src={r.image} alt={r.name} fill className="object-cover group-hover:scale-105 transition-transform duration-300" />
      )}
      <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent" />
      <div className="absolute bottom-0 left-0 p-4 text-white">
        <h3 className="text-xl font-bold">{r.name}</h3>
        <p className="text-sm text-white/80">{r.attraction_count} attractions</p>
      </div>
    </div>
  );
}
```

### Detail page

```tsx
// app/attractions/[slug]/page.tsx
import { attractionDetail } from '@/mockdata';
import type { AttractionDetail } from '@/mockdata';

const a = attractionDetail as AttractionDetail;

export default function AttractionDetailPage() {
  return (
    <article className="max-w-4xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900">{a.name}</h1>
      <p className="text-green-700 font-medium mt-1">
        📍 {a.region.name} · {a.category_display} · {a.difficulty_display}
      </p>
      <p className="mt-4 text-gray-700 leading-relaxed">{a.description}</p>

      {/* Quick facts grid */}
      <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 mt-6">
        <InfoCard icon="⏱" label="Duration" value={a.estimated_duration} />
        <InfoCard icon="💵" label="Entrance Fee" value={a.entrance_fee ? `$${a.entrance_fee} USD` : 'Free'} />
        <InfoCard icon="🗓" label="Best Time" value={a.best_time_to_visit} />
        {a.altitude && <InfoCard icon="📏" label="Altitude" value={`${a.altitude}m`} />}
        <InfoCard icon="✈️" label="Nearest Airport" value={a.nearest_airport} />
      </div>

      {/* Tips */}
      {a.tips.length > 0 && (
        <section className="mt-8">
          <h2 className="text-xl font-bold mb-4">💡 Traveller Tips</h2>
          {a.tips.map((tip) => (
            <div key={tip.id} className="border-l-4 border-amber-400 pl-4 mb-4">
              <p className="font-semibold">{tip.title}</p>
              <p className="text-sm text-gray-600 mt-1">{tip.description}</p>
            </div>
          ))}
        </section>
      )}
    </article>
  );
}

function InfoCard({ icon, label, value }: { icon: string; label: string; value: string }) {
  return (
    <div className="bg-gray-50 rounded-xl p-3">
      <p className="text-xs text-gray-400">{icon} {label}</p>
      <p className="text-sm font-medium text-gray-800 mt-1">{value}</p>
    </div>
  );
}
```

### Weather widget

```tsx
// components/WeatherWidget.tsx
import { weatherMock } from '@/mockdata';
import type { CurrentWeather } from '@/mockdata';

const weather = weatherMock.current_weather as CurrentWeather;

export function WeatherWidget() {
  return (
    <div className="bg-gradient-to-br from-blue-500 to-blue-700 text-white rounded-2xl p-4">
      <p className="text-sm opacity-80">Current weather</p>
      <div className="flex items-end gap-2 mt-1">
        <span className="text-4xl font-bold">{weather.temperature}°C</span>
        <span className="text-sm opacity-80 mb-1">{weather.weather_description}</span>
      </div>
      <div className="grid grid-cols-3 gap-2 mt-4 text-xs">
        <div><span className="opacity-70">Humidity</span><p className="font-semibold">{weather.humidity}%</p></div>
        <div><span className="opacity-70">Wind</span><p className="font-semibold">{weather.wind_speed} km/h</p></div>
        <div><span className="opacity-70">Cloud</span><p className="font-semibold">{weather.cloud_cover}%</p></div>
      </div>
    </div>
  );
}
```

### Swapping mock → real API

When your backend is ready, swap the import source — the type signatures are identical:

```ts
// Before (mock)
import { attractions } from '@/mockdata';

// After (real API with SWR)
import useSWR from 'swr';
import type { AttractionListItem } from '@/mockdata';  // types stay the same

const fetcher = (url: string) => fetch(url).then(r => r.json());

export function useAttractions() {
  return useSWR<AttractionListItem[]>('/api/v1/attractions/', fetcher);
}
```

---

## API endpoints summary

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| `POST` | `/api/v1/auth/register/` | — | Register new user |
| `POST` | `/api/v1/auth/login/` | — | Login → JWT tokens |
| `POST` | `/api/v1/auth/token/refresh/` | — | Refresh access token |
| `GET/PUT/PATCH` | `/api/v1/auth/profile/` | ✅ | Get/update own profile |
| `GET` | `/api/v1/regions/` | — | List all regions |
| `GET` | `/api/v1/regions/:slug/` | — | Region detail |
| `GET` | `/api/v1/attractions/` | — | List attractions (`?search=`, `?ordering=`) |
| `POST` | `/api/v1/attractions/` | ✅ | Create attraction |
| `GET` | `/api/v1/attractions/featured/` | — | Featured attractions |
| `GET` | `/api/v1/attractions/by_category/?category=wildlife` | — | Filter by category |
| `GET` | `/api/v1/attractions/by_region/?region=arusha` | — | Filter by region |
| `GET` | `/api/v1/attractions/:slug/` | — | Attraction detail |
| `PATCH` | `/api/v1/attractions/:slug/` | ✅ | Update attraction |
| `DELETE` | `/api/v1/attractions/:slug/` | ✅ | Delete attraction |
| `GET` | `/api/v1/weather/current/?attraction=:slug` | — | Live weather |
| `GET` | `/api/v1/weather/forecast/?attraction=:slug&days=7` | — | 7-day forecast |
| `GET` | `/api/v1/weather/seasonal/?attraction=:slug` | — | Seasonal patterns |

**Base URL:** `http://localhost:8000`  
**Auth header:** `Authorization: Bearer <access_token>`
