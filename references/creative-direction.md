# Creative direction (обложка, 3 стиля, карусель, identity)

Дистиллят art-director + обязательный стык с техстандартом photos  
([ctr-overlays-4x3.md](ctr-overlays-4x3.md), [meaning-strategy.md](meaning-strategy.md)).

## Когда применять

| Контекст | Как использовать этот файл |
|----------|----------------------------|
| **Режим E** | Полный цикл: 3 обложки → выбор → carousel lock |
| **B2 / новые сеты** | Взять mood/palette/lighting из одного стиля без тройного approve |
| **D storyline** | Carousel brand lock внутри темы; cover energy > warm-up |

## Preview / safe-zone

- Формат Авито: **4:3**; превью поиска часто **~1:1**.
- Весь важный текст и ключевые иконки — внутри safe-zone **1300×1300** @1920×1440 (см. ctr-overlays).
- Не ставить смысл у левого/правого/верхнего/нижнего края кадра.
- Мысленно уменьшить до размера выдачи: если hook/segment не читается — упростить.
- Убрать белые поля/рамки с исходника.

## Обложка: иерархия до генерации

Зафиксировать внутри (не обязательно слать пользователю, кроме режима E по запросу):

1. **Visual hierarchy** — что читать 1 / 2 / 3.
2. **Search anchor** — фраза поиска.
3. **Segment hook** — «это для меня».
4. **Pain/value** — стоп-скролл.
5. **Mood** — premium / friendly / bold / expert / calm / …
6. **Palette** — 2–3 базовых + 1 акцент (из ниши и фото).
7. **Accent** — один главный акцент (сегмент / боль / ценность / дифференциатор): цветной блок, underline, capsule, контраст. Обложка без акцента = слабо.
8. **Infographic metaphor** (опц.) — документы, галочки, инструменты, стрелки; по нише; не перегружать.

Типографика: главный search phrase быстро виден, но не ломает композицию; submeaning **средне-крупный**, не микроподпись.

---

## Три варианта обложки (режим E)

Создать **три отдельных** файла. Запрещено: коллаж, contact sheet, triptych, grid, «3 варианта на одном холсте».

Все три **равносильные** (не один сильный + два черновика). Один смысл (approved), разная подача:

| # | Стиль | Mood / фон / свет |
|---|--------|-------------------|
| 1 | **Deep Contrast** | Premium corporate; тёмный/насыщенный фон; современный studio light; сдержанный glass/3D; без vintage luxury / neon glow |
| 2 | **Clean Minimalism** | Воздух, светлый matte фон; soft studio; clay/matte 3D; сила за счёт типографики и цветных панелей за текстом |
| 3 | **Dynamic Accent** | Смелее, но controlled: тёмный/mid base + 1 main accent + 1 secondary; без кислотных clash-палитр; крупные объекты, диагональ **одна** |

Палитра Dynamic: обычно 1 base + 1 accent + 1 secondary + нейтральный текст. Не мешать blue/red/green/yellow на максимуме.

Каждый вариант: сильная композиция, readable search+pain, focal point, polish, не flat/generic/faceless.

Перед генерацией (внутри): placement субъекта, safe text area, accent, lighting, 3D/icons role, palette sanity (≤1 main + 1 secondary accent), composition sanity (один focal, один movement).

В промпт обложки явно:

```text
Final format 4:3 standalone cover only — not a collage, not a grid, not multiple variants.
Safe text zone for Avito square preview. Use only this text verbatim: "…" and "…".
No other readable text. Clear main accent; submeaning large enough for preview.
Preserve identity and natural body proportions if a person is shown.
Remove white borders. Polished ad quality, non-flat, non-generic.
```

После генерации → **обязательный handoff** (ниже).

---

## Carousel brand lock

После выбора направления обложки — lock для внутренних слайдов:

| Параметр | Правило |
|----------|---------|
| Palette | Один base, text color, **Accent A** (из выбранной обложки) |
| Typography | Один headline scale + один submeaning scale на warm-up |
| Accent method | Один: panel **или** underline **или** color word — не миксовать по слайдам |
| Graphics | Один стиль иконок/линий/теней |
| Photo treatment | Похожие contrast / grading / cutout |
| Tone | Cover premium → internals не хаотичные; cover bold → internals не «сухая презентация» |

Warm-up: **спокойнее** обложки (меньше шума), но не другая «марка».  
CTA-слайд: текст крупнее и прямее, **те же** font character / Accent A / accent method.

Композиции слайдов разные (placement, ритм) — копировать layout обложки нельзя.

### Photo order (исходники пользователя)

```text
1-е internal фото → слайд 2
2-е → слайд 3
…
```

Каждое фото один раз; не reorder / skip / duplicate без запроса. Если числа не хватает — спросить.  
Фото = identity/pose anchor: можно менять фон, свет, панели; человек/товар/место узнаваемы.

---

## Identity и тело (услуги / люди)

- Сохранять лицо, возрастное впечатление, причёску, телосложение, позу, одежду.
- Не redraw в «похожего», не добавлять/убирать людей.
- Не закрывать лицо текстом/графикой.
- Не сжимать/растягивать тело ради текста; при нехватке места — uniform scale, extend background, перенести текст.
- Руки/пальцы/голова — не обрезать неестественно (если исходник не так).

Для услуг: человек **40–60%** кадра; см. [services-photos.md](services-photos.md).

Рискованные объекты на видном месте (битые калькуляторы, читаемые документы с цифрами, fake UI, календари с датами) — избегать; безопаснее папки, галочки, щиты, корзины, абстрактные chart-формы.

---

## Handoff в production (обязательно после E / любой AI-генерации)

1. Center-crop до **4:3** → resize **1920×1440** LANCZOS (без stretch).
2. Текст + плашка только в **1300×1300**; площадь оверлея **10–25%**.
3. Бан-лист и запреты photos (контакты, QR, коллаж-обложка, бан-слова).
4. Сохранить ASCII path: `heroes/{Id}.jpg` и/или `{niche}/premium/{Id}/…`.
5. ImageUrls = длинный cloud-api, разделитель ` | `, ImageNames пусто.
6. Unique firsts; активные объявления не трогать без явного запроса.

Кегли дефолт hero @1920: хук 88–92 / выгода 52–56 / CTA 48–50 — [overlay-hooks.md](overlay-hooks.md).

## Quality checklist (перед сдачей)

- [ ] Смысл из анализа / approved / mass auto-rules
- [ ] Только нужный текст на кадре
- [ ] 4:3 → 1920×1440; safe-zone
- [ ] Preview readability; один акцент на cover
- [ ] E: 3 файла, не коллаж; равная сила
- [ ] Internals: Accent A + одна типографика
- [ ] Identity/тело сохранены
- [ ] CTA whitelist; бан-лист чист
- [ ] Path + ImageUrls готовы к автозагрузке
