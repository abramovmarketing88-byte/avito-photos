# Storyline sets (режим D) — услуги

Когда в брифе/PDF задан **сторитейл по темам**, а не классические 10 сетов × 4.

## Когда применять

- Бухгалтерия, юриды, медицина, консалтинг
- Несколько **смысловых тем** (маркетплейсы, стройка, общее…) × **4–5 кадров** каждая
- В PDF-референсах на каждом слайде **человек + текст**

## Структура

```text
/{DISK_ROOT}/uslugi/
  {theme}/                    # marketplaces | construction | general
    sets/set-01/
      01-hero.jpg
      02-{slug}.jpg
      03-{slug}.jpg
      04-{slug}.jpg
      05-cta.jpg              # опционально
    heroes/{Id}.jpg
```

## Имена файлов

**Жёстко:** имена в папке = ключи в `THEME_SETS` скрипта assign. Пример:

```python
THEME_SETS = {
    "general": ["01-hero", "02-report", "03-trust", "04-support", "05-cta"],
}
# файл на диске: 02-report.jpg  (не 02-support.jpg)
```

## Алгоритм

1. Сгенерировать **N тем × M кадров** с лицом эксперта (reference photos клиента)
2. Crop 4:3 → 1920×1440; залить в `sets/set-01/`
3. На каждую строку Excel:
   - `theme` = keywords Title / winners-matrix / report JSON
   - `heroes/{Id}.jpg` = оверлей(hook из Title + USP темы + CTA) на `01-hero.jpg`
4. ImageUrls:

```text
hero | 02 | 03 | 04 | 05
```

(без повтора `01-hero` в хвосте — он только как уникальный hero)

5. При append: **удалить** старые URL `cloud-api` с тем же path prefix перед записью новых
6. **Активные** AvitoId из backup — skip ImageUrls (если не override в брифе)

## Пример тем (бухгалтерия)

| theme | кадры | смысл |
|-------|-------|-------|
| marketplaces | 5 | селлеры, налоговая, скорость, цикл, CTA |
| construction | 5 | штрафы, под ключ, налоги, индивидуально, CTA |
| general | 5 | без забот, сопровождение, проверка, поддержка, CTA |

**Excluded themes** — из брифа (напр. сезонная отчётность) — не генерировать сеты и title под них.

## Anti-patterns

- Текст на однотонном фоне без человека
- Один hero-файл на все Id без оверлея
- PDF с людьми → генерация без людей
- Дубли cloud-api URL после перегенерации
